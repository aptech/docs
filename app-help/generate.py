"""Offline artifact generation. All writable state lives in /scratch and /out."""
import argparse
from concurrent.futures import ProcessPoolExecutor
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tarfile
import time
import xml.etree.ElementTree as ET

from inputs import verify

EXT = {'.png', '.jpg', '.jpeg', '.html', '.htm', '.css', '.js', '.gif',
       '.htc', '.svg', '.woff2', '.woff', '.ttf', '.eot'}

def run(args, **kw):
    print('+', ' '.join(map(str, args)), flush=True)
    subprocess.run(list(map(str, args)), check=True, **kw)

def clean(args):
    script, begin, end, stage = args
    run(['python', script, begin, end], cwd=stage, stdout=subprocess.DEVNULL)

def transform(p):
    text = p.read_text(errors='strict')
    if p.suffix == '.html':
        # Preserve the original packager's flat URL contract, without mangling
        # absolute outbound links or creating new network dependencies.
        text = re.sub(r' &mdash; GAUSS \d+ documentation', '', text)
        text = re.sub(r'\bCR-(\w+)\.html', lambda m: m[1].lower()+'.html', text)
        text = text.replace('GG.8-InteractingwithPlots.html', 'GG.8.0-InteractingwithPlots.html')
        text = text.replace('async="async" ', '')
        def attr(m):
            key, value = m[1], m[2]
            if re.search(r'https://[^\s]+mathjax[^\s]+(?:latest\.js|MathJax\.js)', value, re.I):
                return key+'="MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"'
            if value.startswith(('http:', 'https:', '//', 'data:', 'mailto:', '#', 'javascript:')):
                return m[0]
            value = value.rsplit('/', 1)[-1]
            value = re.sub(r'\.htm(?=[?#]|$)', '.html', value)
            value = re.sub(r'^index\.html', 'welcome.html', value)
            value = value.replace('Styles.css', 'bootstrap.min.css')
            return key+'="'+value+'"'
        text = re.sub(r'(src|href)="([^"]+)"', attr, text)
        # These website navigation endpoints are deliberately not shipped.
        text = re.sub(r'<link\b[^>]*href="(?:genindex|search)\.html"[^>]*>', '', text)
    else:
        text = re.sub(r'url\(([\'\"]?)([^)]+)\)',
                      lambda m: m[0] if m[2].startswith(('data:', 'http:', 'https:', '//'))
                      else 'url('+m[1]+m[2].rsplit('/', 1)[-1]+')', text)
    p.write_text(text)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--jobs', type=int, default=2)
    a = p.parse_args()
    if not 1 <= a.jobs <= 16:
        p.error('--jobs must be between 1 and 16')
    start = time.monotonic()
    root, work, out = Path('/inputs'), Path('/scratch'), Path('/out')
    lock = verify(root)
    if any(out.iterdir()):
        raise ValueError('Output directory must be empty')
    pkg = root/'packaging'
    stage = work/'build'
    stage.mkdir()
    html = work/'html'
    # The archive conf.py and custom GAUSS domain/translator remain authoritative.
    run(['python', '/opt/app-help/html_build.py', root/'docs/docs', html, str(a.jobs)])
    collisions = []
    origins = {}
    def copy(files):
        for f in sorted(files):
            if not f.is_file() or f.suffix.lower() not in EXT:
                continue
            name = f.stem+'.html' if f.suffix == '.htm' else f.name
            if name in origins and (stage/name).read_bytes() != f.read_bytes():
                collisions.append([name, origins[name], str(f)])
            shutil.copyfile(f, stage/name)
            origins[name] = str(f)
    copy((pkg/'etc/welcome').rglob('*'))
    copy((pkg/'HTML5').rglob('*'))
    for f in stage.glob('CR-*.htm*'):
        f.unlink()
    (stage/'ChangeLog.html').unlink(missing_ok=True)
    copy(f for f in html.iterdir() if f.name not in ('index.html', 'genindex.html'))
    copy((html/'data-management').glob('*'))
    copy((html/'_static').rglob('*'))
    copy((html/'_images').rglob('*'))
    copy((pkg/'etc/fonts').rglob('*'))
    copy((pkg/'etc/mathjax').rglob('*'))
    with (stage/'theme_override.css').open('a') as f:
        f.write('\n.wy-nav-content-wrap { margin-left: 0px !important; } '
                'div.wy-nav-content { max-width: initial !important; } '
                'div.section#command-reference > div.toctree-wrapper:first-of-type '
                '{ display: none !important; }\n')
    for f in sorted(stage.iterdir()):
        if f.suffix in ('.html', '.css'):
            transform(f)
    ranges = [('_','a'), ('b','c'), ('d','f'), ('g','i'), ('j','l'),
              ('m','o'), ('p','r'), ('s','u'), ('v','z')]
    with ProcessPoolExecutor(max_workers=a.jobs) as pool:
        list(pool.map(clean, [(pkg/'clean_sphinx.py', b, e, stage) for b,e in ranges]))
    # A full, pinned MathJax tree is necessary: the old script copied a loader
    # but referred to an absent MathJax/ directory.
    math = stage/'MathJax'
    math.mkdir()
    with tarfile.open(root/'mathjax-2.7.9.tgz') as tar:
        for member in tar.getmembers():
            parts = Path(member.name).parts
            if len(parts) < 2:
                continue
            rel = Path(*parts[1:])
            if rel.parts[0] not in ('MathJax.js', 'config', 'extensions', 'jax',
                                    'fonts', 'localization', 'LICENSE'):
                continue
            if member.issym() or member.islnk() or '..' in rel.parts:
                raise ValueError('Unsafe MathJax archive member')
            dest = math/rel
            if member.isfile():
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(tar.extractfile(member).read())
    for name in ['help.properties.head', 'help.properties.tail']:
        shutil.copyfile(pkg/name, work/name)
    head = work/'help.properties.head'
    head.write_text(head.read_text().replace('|GG.8-InteractingwithPlots',
                                            '|GG.8.0-InteractingwithPlots'))
    run(['python', pkg/'genhelpproperties.py'], cwd=work)
    run(['python', pkg/'help.py'], cwd=work)
    project = ET.parse(stage/'gauss.qhp')
    files = project.find('.//files')
    files.clear()
    for f in sorted(stage.rglob('*')):
        if f.is_file() and f.name != 'gauss.qhp':
            ET.SubElement(files, 'file').text = f.relative_to(stage).as_posix()
    project.write(stage/'gauss.qhp', encoding='utf-8', xml_declaration=True)
    collection = ET.parse(pkg/'gauss.qhcp')
    # Retain every collection setting, but keep both generated artifacts together.
    collection.find('.//generate/file/input').text = str(stage/'gauss.qhp')
    collection.find('.//generate/file/output').text = 'gauss.qch'
    collection.find('.//register/file').text = 'gauss.qch'
    collection.write(work/'gauss.qhcp', encoding='utf-8', xml_declaration=True)
    run(['/usr/lib/qt5/bin/qhelpgenerator', work/'gauss.qhcp', '-o', work/'gauss.qhc'])
    for name in ['gauss.qch', 'gauss.qhc', 'help.properties']:
        shutil.copyfile(work/name, out/name)
    shutil.copyfile(stage/'gauss.qhp', out/'gauss.qhp')
    shutil.copyfile(root/'inputs.lock.json', out/'inputs.lock.json')
    for src in ['/opt/native-packages.lock', '/opt/python-packages.lock']:
        shutil.copyfile(src, out/Path(src).name)
    (out/'generation.json').write_text(json.dumps({
        'seconds': time.monotonic()-start, 'jobs': a.jobs,
        'namespace': project.findtext('namespace'), 'collisions': collisions,
        'provenance': lock['provenance']}, indent=2))
    run(['python', '/opt/app-help/validate.py', out,
         '--baseline', root/'baseline/gauss.qch'])
    # Probe a disposable collection copy: search indexing must not alter delivery.
    probe = work/'probe'
    probe.mkdir()
    for name in ['gauss.qch', 'gauss.qhc']:
        shutil.copyfile(out/name, probe/name)
    run(['/usr/bin/python3', '/opt/app-help/qt_probe.py', probe, out])

if __name__ == '__main__':
    main()
