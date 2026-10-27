"""Compare repeat builds by logical content, normalizing Qt metadata and IDs."""
import argparse
import hashlib
import json
from pathlib import Path
import sqlite3

def logical(path):
    c = sqlite3.connect('file:'+str(path)+'?mode=ro', uri=True)
    attributes = dict(c.execute('select Id, Name from FilterAttributeTable'))
    result = {}
    for (table,) in c.execute("select name from sqlite_master where type='table' order by name"):
        rows = c.execute('select * from "'+table.replace('"', '""')+'"').fetchall()
        columns = [r[1] for r in c.execute('pragma table_info("'+table+'")')]
        if path.suffix == '.qhc' and table == 'SettingsTable':
            rows = [r for r in rows if r[0] not in ('LastRegisterTime', 'CreationTime')]
        if path.suffix == '.qhc' and table == 'TimeStampTable':
            # QCH filesystem mtime is captured at registration, not help content.
            rows = [r[:-1] for r in rows]
        if table == 'FilterAttributeTable':
            rows = [(r[1],) for r in rows]
        else:
            # Qt obtains attributes from a QSet; ID assignment is intentionally
            # not stable. Compare the associated names, preserving relationships.
            rows = [tuple(attributes[x] if columns[i] == 'FilterAttributeId' else x
                          for i, x in enumerate(row)) for row in rows]
        normalized = [[{'blob_sha256': hashlib.sha256(x).hexdigest()}
                       if isinstance(x, bytes) else x for x in row] for row in rows]
        result[table] = sorted(normalized, key=lambda r: json.dumps(r, sort_keys=True))
    return result

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('first', type=Path)
    p.add_argument('second', type=Path)
    a = p.parse_args()
    report = {}
    for name in ['gauss.qch', 'gauss.qhc']:
        first, second = a.first/name, a.second/name
        x, y = logical(first), logical(second)
        report[name] = {'byte_identical': first.read_bytes() == second.read_bytes(),
                        'logical_content_identical': x == y,
                        'different_tables': [k for k in x.keys() | y.keys() if x.get(k) != y.get(k)]}
    print(json.dumps(report, indent=2))
    assert all(x['logical_content_identical'] for x in report.values()), 'Repeat builds differ'
