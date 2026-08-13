# Scan admin .pyc bytecode for admin-hash related strings (ASCII only).
from __future__ import print_function
import os

ADMIN_DIR = r'C:\fh2_1\mods\fh2\python\admin'
PATTERNS = (
    'ADMINS_HIGH',
    'ADMINS_MID',
    'ADMINS_LOW',
    'get_admin_level',
    'with Hash',
    'getHash',
    'admins_high',
    'player_hash',
    'in ADMINS',
)


def scan_file(path):
    data = open(path, 'rb').read()
    hits = []
    for p in PATTERNS:
        if p.encode('ascii') in data:
            hits.append(p)
    return hits


def main():
    for root, _dirs, files in os.walk(ADMIN_DIR):
        for name in files:
            if not name.endswith('.pyc'):
                continue
            path = os.path.join(root, name)
            hits = scan_file(path)
            if hits:
                rel = path[len(ADMIN_DIR) + 1:]
                print('%s: %s' % (rel, ', '.join(hits)))


if __name__ == '__main__':
    main()
