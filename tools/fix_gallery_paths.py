#!/usr/bin/env python3
"""批量替换 gallery_python 中的硬编码路径为包相对路径。"""
import os
import re

GALLERY_DIR = r'D:\CODE\sci-plot\src\gallery_python'

# 硬编码路径模式
OLD_PATTERN = r"csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'"
NEW_PATH = "csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')"

# 需要添加 import os 的检测
IMPORT_OS = "import os"
IMPORT_OS_RE = re.compile(r'^import os\b', re.MULTILINE)

modified = 0
skipped = 0
no_import_os = 0

for root, dirs, files in os.walk(GALLERY_DIR):
    for fname in files:
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否有硬编码路径
        if "D:\\CODE\\sci-plot\\tests\\data" not in content:
            skipped += 1
            continue

        # 替换路径
        content = content.replace(OLD_PATTERN, NEW_PATH)

        # 检查并添加 import os
        if not IMPORT_OS_RE.search(content):
            # 在第一个 import 后添加 import os
            lines = content.split('\n')
            insert_pos = None
            for i, line in enumerate(lines):
                # 找第一个 import 行的后面
                if line.startswith('import ') or line.startswith('from '):
                    # 如果当前行是 import os，跳过
                    if line.strip() == 'import os':
                        insert_pos = None
                        break
                    insert_pos = i + 1
                elif line.strip() == '' and insert_pos is not None:
                    insert_pos = i + 1

            if insert_pos is not None:
                # 检查是否在 import 块之后插入
                lines.insert(insert_pos, 'import os')
                content = '\n'.join(lines)
                no_import_os += 1

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

        modified += 1
        print(f'  [OK] {os.path.relpath(fpath, GALLERY_DIR)}')

print(f'\n=== 完成 ===')
print(f'修改: {modified}')
print(f'跳过（无硬编码路径）: {skipped}')
print(f'已添加 import os: {no_import_os}')