import sys
from sphinx.application import Sphinx

source, output, jobs, release = sys.argv[1:]
overrides = {}
if release:
    overrides = {'version': release, 'release': release,
                 'html_short_title': 'GAUSS '+release+' documentation',
                 'html_title': 'GAUSS '+release+' documentation | Aptech'}
app = Sphinx(source, source, output, '/scratch/doctrees', 'html',
             parallel=int(jobs), freshenv=True, confoverrides=overrides)
print('Effective theme directories:', app.builder.theme.get_theme_dirs(), flush=True)
app.build(force_all=True)
if app.statuscode:
    raise SystemExit(app.statuscode)
