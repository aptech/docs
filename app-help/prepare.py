"""Prepare a sealed input bundle. This step may use network; build.sh cannot.

Packaging and baseline directories must be explicit snapshots acquired by the
caller. No source checkout is updated, and no production script is executed.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request

from inputs import hashes, MATHJAX_SHA256

def archive(repo, revision, dest):
    if len(revision) != 40 or any(c not in '0123456789abcdef' for c in revision):
        raise ValueError('Use a complete immutable Git commit, not a branch: '+revision)
    data = subprocess.check_output(['git', '-C', str(repo), 'archive', revision])
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        for item in tar.getmembers():
            if item.name.startswith('/') or '..' in Path(item.name).parts or item.issym() or item.islnk():
                raise ValueError('Unsafe/symlink archive entry: '+item.name)
        tar.extractall(dest)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--docs-repo', required=True, type=Path)
    p.add_argument('--docs-revision', required=True)
    p.add_argument('--packaging', required=True, type=Path)
    p.add_argument('--baseline', required=True, type=Path)
    p.add_argument('--packaging-provenance', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    a = p.parse_args()
    a.output.mkdir(parents=True, exist_ok=False)
    archive(a.docs_repo, a.docs_revision, a.output/'docs')
    submodules = {
        'docs/_themes/sphinx_rtd_theme': ('https://github.com/readthedocs/sphinx_rtd_theme',
                                        'd64dadf1ceec4f9ff6c1ca2d3ea4c3d0fdb0e8d2'),
        'docs/textbook-examples': ('https://github.com/aptech/gauss-textbook-examples',
                                  '68800eb0782bb9d3dc8354ed19bc4084525a758f'),
        'docs/tspdlib': ('https://github.com/aptech/tspdlib.git',
                        'ed4199d0a6821604940a108aa4664813ae551843')}
    # Explicit overrides reproduce archive inputs; never --remote or moving refs.
    for path, (url, revision) in submodules.items():
        with tempfile.TemporaryDirectory(prefix='gauss-help-git-') as tmp:
            subprocess.run(['git', 'clone', '--quiet', '--no-checkout', url, tmp], check=True)
            archive(tmp, revision, a.output/'docs'/path)
    pkg = a.output/'packaging'
    pkg.mkdir()
    for name in ['HTML5', 'etc', 'clean_sphinx.py', 'genhelpproperties.py', 'help.py',
                 'help.properties.head', 'help.properties.tail', 'gauss.qhcp',
                 'mkhelp.sh', 'requirements.txt']:
        src, dest = a.packaging/name, pkg/name
        if src.is_dir():
            shutil.copytree(src, dest, symlinks=True)
        else:
            shutil.copyfile(src, dest, follow_symlinks=False)
    (a.output/'baseline').mkdir()
    for name in ['gauss.qch', 'gauss.qhc']:
        shutil.copyfile(a.baseline/name, a.output/'baseline'/name)
    url = 'https://registry.npmjs.org/mathjax/-/mathjax-2.7.9.tgz'
    data = urllib.request.urlopen(url, timeout=60).read()
    if hashlib.sha256(data).hexdigest() != MATHJAX_SHA256:
        raise ValueError('MathJax checksum mismatch')
    (a.output/'mathjax-2.7.9.tgz').write_bytes(data)
    provenance = {
        'docs': {'repository': subprocess.check_output(['git', '-C', str(a.docs_repo),
                'remote', 'get-url', 'origin'], text=True).strip(), 'revision': a.docs_revision},
        'submodules': submodules,
        'packaging': json.loads(a.packaging_provenance.read_text()),
        'MathJax': {'url': url, 'sha256': MATHJAX_SHA256}}
    (a.output/'inputs.lock.json').write_text(json.dumps({
        'provenance': provenance, 'sha256': hashes(a.output)}, indent=2, sort_keys=True))
    print('Prepared:', a.output)

if __name__ == '__main__':
    main()
