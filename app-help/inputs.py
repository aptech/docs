"""Seal/verify explicit, self-contained inputs. No credentials or source writes."""
import argparse
import hashlib
import json
from pathlib import Path

REQUIRED = ['docs/docs/conf.py', 'packaging/clean_sphinx.py',
            'docs/docs/tspdlib/docs/tspdlib-landing.rst',
            'packaging/genhelpproperties.py', 'packaging/help.py',
            'packaging/help.properties.head', 'packaging/help.properties.tail',
            'packaging/gauss.qhcp', 'packaging/etc/welcome/welcome.html',
            'mathjax-2.7.9.tgz', 'baseline/gauss.qch', 'baseline/gauss.qhc']
MATHJAX_SHA256 = '7131e739848edc14aa661a5516995866b81a477fab8b039d7cc324930e71f786'

def hashes(root):
    result = {}
    for p in sorted(root.rglob('*')):
        if p.is_symlink():
            raise ValueError('Input symlinks are not allowed: ' + str(p))
        if p.is_file() and p != root/'inputs.lock.json':
            result[p.relative_to(root).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    for name in REQUIRED:
        if name not in result:
            raise ValueError('Missing required input: ' + name)
    if not any(n.startswith('packaging/HTML5/') for n in result):
        raise ValueError('Missing legacy HTML5 inputs')
    if result['mathjax-2.7.9.tgz'] != MATHJAX_SHA256:
        raise ValueError('MathJax archive checksum mismatch')
    return result

def verify(root):
    lock = json.loads((root / 'inputs.lock.json').read_text())
    if hashes(root) != lock['sha256']:
        raise ValueError('Inputs differ from inputs.lock.json; prepare and review a new snapshot')
    return lock

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['seal', 'verify'])
    p.add_argument('directory', type=Path)
    p.add_argument('--provenance', type=Path, help='Required JSON file when sealing')
    a = p.parse_args()
    if a.action == 'verify':
        verify(a.directory)
    else:
        if not a.provenance:
            p.error('--provenance is required when sealing')
        dest = a.directory / 'inputs.lock.json'
        with dest.open('x') as f:
            json.dump({'provenance': json.loads(a.provenance.read_text()),
                       'sha256': hashes(a.directory)}, f, indent=2, sort_keys=True)
    print('Inputs ' + a.action + ': OK')
