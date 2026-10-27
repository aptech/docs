import sys
from sphinx.application import Sphinx

source, output, jobs = sys.argv[1:]
app = Sphinx(source, source, output, '/scratch/doctrees', 'html',
             parallel=int(jobs), freshenv=True)
print('Effective theme directories:', app.builder.theme.get_theme_dirs(), flush=True)
app.build(force_all=True)
if app.statuscode:
    raise SystemExit(app.statuscode)
