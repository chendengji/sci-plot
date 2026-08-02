#!/usr/bin/env python3
"""修复剩余的不同数据文件路径。"""
import os
import re

GALLERY_DIR = r'D:\CODE\sci-plot\src\gallery_python'

# 所有需要替换的模式
REPLACEMENTS = [
    ("standard_categorized.csv", "standard_categorized.csv"),
    ("standard_grid.csv", "standard_grid.csv"),
    ("standard_xy.csv", "standard_xy.csv"),
]

_import_os_re = re.compile(r'^import os\b', re.MULTILINE)

modified = 0
for root, dirs, files in os.walk(GALLERY_DIR):
    for fname in files:
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if "D:\\CODE\\sci-plot\\tests\\data" not in content:
            continue

        changed = False
        for data_file, _ in REPLACEMENTS:
            old = f"csv_path = r'D:\\CODE\\sci-plot\\tests\\data\\{data_file}'"
            new = f"csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', '{data_file}')"
            if old in content:
                content = content.replace(old, new)
                changed = True

        if not changed:
            continue

        # Add import os if missing
        if not _import_os_re.search(content):
            lines = content.split('\n')
            insert_pos = None
            for i, line in enumerate(lines):
                if line.startswith('import ') or line.startswith('from '):
                    if line.strip() == 'import os':
                        insert_pos = None
                        break
                    insert_pos = i + 1
                elif line.strip() == '' and insert_pos is not None:
                    insert_pos = i + 1
            if insert_pos is not None:
                lines.insert(insert_pos, 'import os')
                content = '\n'.join(lines)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        modified += 1
        print(f'  [OK] {os.path.relpath(fpath, GALLERY_DIR)}')

print(f'\n修改: {modified}')