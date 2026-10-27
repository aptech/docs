"""Inspect actual Qt help databases and compare content with an existing QCH."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
import posixpath
from pathlib import Path
import re
import sqlite3
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zlib

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.text = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and 'name' in a:
            self.ids.add(a['name'])
        for attr in ('src', 'href'):
            if attr in a:
                self.links.append((tag, attr, a[attr]))
    def handle_data(self, data):
        self.text.append(data)

def read_qch(path):
    c = sqlite3.connect('file:'+str(path)+'?mode=ro', uri=True)
    assert c.execute('pragma integrity_check').fetchone() == ('ok',), str(path)
    files = {}
    for name, blob in c.execute('select n.Name, d.Data from FileNameTable n '
                               'join FileDataTable d on d.Id=n.FileId'):
        if not name:
            continue
        data = zlib.decompress(blob[4:])
        assert len(data) == int.from_bytes(blob[:4], 'big')
        files[name] = data
    namespace = c.execute('select Name from NamespaceTable').fetchone()[0]
    return c, files, namespace

def audit(files):
    broken, external, anchors = set(), set(), set()
    parsed = {}
    for name, data in files.items():
        if name.endswith(('.html', '.htm')):
            doc = Links()
            doc.feed(data.decode('utf-8'))
            parsed[name] = doc
    for name, doc in parsed.items():
        for tag, attr, value in doc.links:
            url = urlsplit(value)
            if url.scheme or url.netloc:
                if attr == 'src' or (tag == 'link' and url.path.endswith('.css')):
                    external.add((name, value))
                continue
            target = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(url.path))) if url.path else name
            if target not in files:
                broken.add((name, value))
            elif url.fragment and target in parsed and unquote(url.fragment) not in parsed[target].ids:
                anchors.add((name, value))
    for name, data in files.items():
        if name.endswith('.css'):
            for value in re.findall(r'url\([\'\"]?([^\)\'\"]+)', data.decode('utf-8')):
                u = urlsplit(value)
                if u.scheme or u.netloc or not u.path:
                    continue
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(u.path)))
                if target not in files:
                    broken.add((name, value))
    return broken, external, anchors

def main():
    p = argparse.ArgumentParser()
    p.add_argument('output', type=Path)
    p.add_argument('--baseline', type=Path, required=True)
    a = p.parse_args()
    c, files, namespace = read_qch(a.output/'gauss.qch')
    old, baseline, old_ns = read_qch(a.baseline)
    assert namespace == old_ns, (namespace, old_ns)
    qhc = sqlite3.connect('file:'+str(a.output/'gauss.qhc')+'?mode=ro', uri=True)
    assert qhc.execute('pragma integrity_check').fetchone() == ('ok',)
    assert qhc.execute('select Name, FilePath from NamespaceTable').fetchall() == [(namespace, 'gauss.qch')]
    project = ET.parse(a.output/'gauss.qhp')
    toc = project.findall('.//toc//section')
    keywords = c.execute('select Name, Identifier from IndexTable').fetchall()
    assert any(ident == 'ols' for name, ident in keywords), 'Missing context-help identifier ols'
    missing_toc = sorted({x.attrib['ref'] for x in toc if x.attrib['ref'].split('#')[0] not in files})
    assert c.execute('select count(*) from ContentsTable').fetchone()[0] > 0
    required = ['welcome.html', 'index.html', 'IN-Introduction.html', 'ols.html',
                'cdfncdfnc.html', 'command-reference.html', 'MathJax/MathJax.js',
                'MathJax/config/TeX-AMS-MML_HTMLorMML.js']
    for name in required:
        assert name in files and len(files[name]) > 100, name
    assert files['pxyf1.png'] == baseline['pxyf1.png'], 'Representative plot image changed'
    broken, external, anchors = audit(files)
    old_broken, old_external, old_anchors = audit(baseline)
    report = {
        'namespace': namespace, 'files': len(files), 'baseline_files': len(baseline),
        'missing_toc_targets': missing_toc,
        'toc_entries': len(toc), 'keywords': len(keywords),
        'baseline_keywords': old.execute('select count(*) from IndexTable').fetchone()[0],
        'missing_baseline_files': sorted(set(baseline)-set(files)),
        'broken_local_references': sorted(broken),
        'new_broken_local_references': sorted(broken-old_broken),
        'external_resources': sorted(external),
        'new_external_resources': sorted(external-old_external),
        'missing_anchors': sorted(anchors),
        'new_missing_anchors': sorted(anchors-old_anchors),
        'representative_comparison': {},
        'content_sha256': {n: hashlib.sha256(v).hexdigest() for n,v in sorted(files.items())},
    }
    for name in required[:6]:
        doc, prev = Links(), Links()
        doc.feed(files[name].decode())
        prev.feed(baseline.get(name, b'').decode())
        report['representative_comparison'][name] = {
            'bytes': len(files[name]), 'baseline_bytes': len(baseline.get(name, b'')),
            'same_visible_text': ' '.join(' '.join(doc.text).split()) == ' '.join(' '.join(prev.text).split())}
    (a.output/'validation.json').write_text(json.dumps(report, indent=2, sort_keys=True))
    print(json.dumps({k:report[k] for k in ('namespace','files','toc_entries','keywords')}, indent=2))
    assert not missing_toc, missing_toc
    assert not report['new_external_resources'], 'New external resources; see validation.json'
    assert not report['new_broken_local_references'], 'New missing resources/links; see validation.json'

if __name__ == '__main__':
    main()
