"""Measure the entire cgroup, including Sphinx/cleanup/Qt children and cache."""
import json
from pathlib import Path
import subprocess
import sys
import threading
import time

cg = Path('/sys/fs/cgroup')
if any(Path('/out').iterdir()):
    raise SystemExit('Output directory must be empty')
peak_sample = 0
stop = threading.Event()
def sample():
    global peak_sample
    while not stop.is_set():
        try:
            peak_sample = max(peak_sample, int((cg/'memory.current').read_text()))
        except OSError:
            pass
        stop.wait(.02)

t = threading.Thread(target=sample, daemon=True)
t.start()
start = time.monotonic()
result = subprocess.run(['python', '/opt/app-help/generate.py', *sys.argv[1:]])
stop.set()
t.join()
metrics = {'elapsed_seconds': time.monotonic()-start, 'exit_code': result.returncode,
           'sampled_cgroup_peak_bytes': peak_sample, 'sample_interval_seconds': .02}
for name in ['memory.peak', 'memory.max', 'memory.events', 'cpu.stat']:
    p = cg/name
    metrics[name] = p.read_text().strip() if p.exists() else None
metrics['peak_method'] = 'kernel cgroup memory.peak' if metrics['memory.peak'] else 'sampled cgroup memory.current (lower bound)'
Path('/out/resources.json').write_text(json.dumps(metrics, indent=2))
sys.exit(result.returncode)
