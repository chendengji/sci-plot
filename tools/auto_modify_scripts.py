#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统化改造脚本：将所有 gallery_python 脚本改为使用标准化数据
"""
import os
import re
import pandas as pd

# 标准化数据路径（相对本工具所在目录）
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tests', 'data')

# 数据文件映射
DATA_FILES = {
    'standard_xy.csv': 'xy',          # 成对数据 x, y, group
    'standard_xy_simple.csv': 'xy_simple',  # 简化数据 x, y
    'standard_categorized.csv': 'categorized',  # 分类数据 category, value
    'standard_grid.csv': 'grid',      # 网格数据 x, y, z
    'standard_vector.csv': 'vector',  # 向量数据 x, y, u, v
    'standard_3d.csv': '3d',          # 3D 数据 x, y, z, category
    'standard_ecdf.csv': 'ecdf',      # ECDF 数据 group, value
}

# 读取所有数据
data_cache = {}
for fname, dtype in DATA_FILES.items():
    path = os.path.join(DATA_DIR, fname)
    if os.path.exists(path):
        data_cache[dtype] = pd.read_csv(path)
        print(f'Loaded {fname}: {data_cache[dtype].shape}')

# 定义图表类型到数据类型的映射
TYPE_MAP = {
    # 线图 -> xy
    'line': 'xy',
    'curve': 'xy',
    'parametric': 'xy',
    'simple_plot': 'xy_simple',
    'scatter': 'xy',
    'fill_between': 'xy',
    'stackplot': 'xy',
    'stairs': 'xy_simple',
    'stem': 'xy_simple',
    'multicolored_line': 'xy',
    'scatter_hist': 'xy',
    
    # 柱状图 -> categorized
    'bar': 'categorized',
    'barchart': 'categorized',
    'barh': 'categorized',
    'stackbar': 'categorized',
    
    # 直方图/分布 -> categorized
    'hist': 'categorized',
    'distribution': 'categorized',
    'ecdf': 'ecdf',
    
    # 统计图表 -> categorized
    'boxplot': 'categorized',
    'violin': 'categorized',
    'errorbar': 'categorized',
    'hexbin': 'xy',
    'pie': 'categorized',
    
    # 3D 图表 -> 3d 或 grid
    'surface': 'grid',
    'contour': 'grid',
    'scatter3d': '3d',
    'bar3d': '3d',
    'wireframe': 'grid',
    'quiver3d': 'vector',
    'streamplot': 'vector',
    'voxels': 'grid',
    'trisurf': 'grid',
    
    # 极坐标 -> xy
    'polar': 'xy',
    
    # 其他
    'image': 'grid',
    'pcolormesh': 'grid',
    'imshow': 'grid',
}


def detect_chart_type(script_path):
    """检测脚本的图表类型"""
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fname = os.path.basename(script_path)
    lower_content = content.lower()
    lower_fname = fname.lower()
    
    # 根据文件名和内容判断类型
    if 'line' in lower_fname or 'plot' in lower_fname:
        return 'line'
    elif 'scatter' in lower_fname:
        return 'scatter'
    elif 'bar' in lower_fname:
        return 'bar'
    elif 'hist' in lower_fname or 'distribution' in lower_content:
        return 'hist'
    elif 'box' in lower_fname or 'violin' in lower_fname:
        return 'boxplot'
    elif '3d' in lower_fname or 'surface' in lower_fname:
        return 'surface'
    elif 'contour' in lower_fname:
        return 'contour'
    elif 'pie' in lower_fname:
        return 'pie'
    elif 'quiver' in lower_fname:
        return 'quiver3d'
    elif 'stream' in lower_fname:
        return 'streamplot'
    elif 'scatter3d' in lower_fname:
        return 'scatter3d'
    elif 'bar3d' in lower_fname:
        return 'bar3d'
    else:
        # 根据内容判断
        if 'plt.scatter' in content or 'ax.scatter' in content:
            return 'scatter'
        elif 'plt.bar' in content or 'ax.bar' in content:
            return 'bar'
        elif 'plt.hist' in content or 'ax.hist' in content:
            return 'hist'
        elif 'plt.plot' in content or 'ax.plot' in content:
            return 'line'
        elif 'projection="3d"' in content or "projection='3d'" in content:
            return 'surface'
        else:
            return 'line'


def generate_data_usage(dtype):
    """生成数据使用代码"""
    data_files = {
        'xy': 'standard_xy.csv',
        'xy_simple': 'standard_xy_simple.csv',
        'categorized': 'standard_categorized.csv',
        'grid': 'standard_grid.csv',
        'vector': 'standard_vector.csv',
        '3d': 'standard_3d.csv',
        'ecdf': 'standard_ecdf.csv',
    }
    fname = data_files.get(dtype, 'standard_xy.csv')
    return f'''
# 使用标准化数据
csv_path = r'{os.path.join(DATA_DIR, fname)}'
data = pd.read_csv(csv_path)
'''


def modify_script(script_path, target_dtype):
    """修改单个脚本"""
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 检查是否已使用标准化数据
    if 'standard_' in content and 'pd.read_csv' in content:
        return False, "Already uses standardized data"
    
    # 查找并替换随机数据生成代码
    # 移除 np.random 相关代码
    content = re.sub(r'np\.random\.[a-z_]+\([^)]+\)', 'generate_random_data()', content)
    
    # 移除 matplotlib.style.use 中的 penguin 数据引用
    content = content.replace("'penguins'", "'standard_data'")
    
    # 添加数据导入
    data_import = '''
import pandas as pd

# 读取标准化数据
''' + generate_data_usage(target_dtype)
    
    # 在 imports 后插入数据导入
    if 'import pandas' in content:
        content = content.replace('import pandas as pd', 'import pandas as pd\n' + data_import.strip())
    elif 'import matplotlib' in content:
        # 在第一个 import 后插入
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'import matplotlib' in line or 'import numpy' in line:
                lines.insert(i + 1, '\nimport pandas as pd')
                lines.insert(i + 2, '# 读取标准化数据')
                lines.insert(i + 3, f"csv_path = r'{os.path.join(DATA_DIR, DATA_FILES.get(target_dtype, 'standard_xy.csv'))}'")
                lines.insert(i + 4, 'data = pd.read_csv(csv_path)')
                content = '\n'.join(lines)
                break
        else:
            content = data_import + '\n' + content
    
    # 替换数据使用
    if target_dtype == 'xy':
        # xy 数据
        content = re.sub(r'x\s*=\s*[^;,\n]+', 'x = data["x"].values', content)
        content = re.sub(r'y\s*=\s*[^;,\n]+', 'y = data["y"].values', content)
    elif target_dtype == 'xy_simple':
        content = re.sub(r'x\s*=\s*[^;,\n]+', 'x = data["x"].values', content)
        content = re.sub(r'y\s*=\s*[^;,\n]+', 'y = data["y"].values', content)
    elif target_dtype == 'categorized':
        # 分类数据
        if 'group' not in content:
            content += '\n\n# 按类别分组计算统计量\ngroups = data["category"].unique()\nmeans = [data[data["category"] == g]["value"].mean() for g in groups]\n'
    elif target_dtype == 'grid':
        # 网格数据
        content += '\n\n# 将长格式数据转换为网格格式\nx_unique = np.sort(data["x"].unique())\ny_unique = np.sort(data["y"].unique())\nX, Y = np.meshgrid(x_unique, y_unique)\nZ = data["z"].values.reshape(len(y_unique), len(x_unique))\n'
    elif target_dtype == 'vector':
        # 向量数据
        content += '\n\n# 向量场数据\nX = data["x"].values.reshape(int(len(data)**0.5), int(len(data)**0.5))\nY = data["y"].values.reshape(int(len(data)**0.5), int(len(data)**0.5))\nU = data["u"].values.reshape(int(len(data)**0.5), int(len(data)**0.5))\nV = data["v"].values.reshape(int(len(data)**0.5), int(len(data)**0.5))\n'
    elif target_dtype == '3d':
        # 3D 数据
        content += '\n\n# 3D 数据\nx = data["x"].values\ny = data["y"].values\nz = data["z"].values\ncategories = data["category"].values\n'
    elif target_dtype == 'ecdf':
        # ECDF 数据
        content += '\n\n# ECDF 数据\ngroups = data["group"].unique()\n'
    
    # 添加改造说明注释
    remark = '''
#
# **改造说明**: 原始脚本使用随机数据，已改造为使用标准化 CSV 数据文件。
#
'''
    
    # 保存修改后的文件
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, "Modified"


def main():
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'gallery_python')
    
    # 收集所有脚本
    scripts = []
    for root, dirs, files in os.walk(base):
        for f in files:
            if f.endswith('.py'):
                scripts.append(os.path.join(root, f))
    
    print(f'Found {len(scripts)} scripts to process')
    
    # 处理每个脚本
    modified = 0
    skipped = 0
    
    for script_path in scripts:
        # 检测图表类型
        chart_type = detect_chart_type(script_path)
        target_dtype = TYPE_MAP.get(chart_type, 'xy')
        
        # 修改脚本
        success, msg = modify_script(script_path, target_dtype)
        if success:
            modified += 1
            print(f'Modified: {os.path.relpath(script_path, base)} (type: {chart_type})')
        else:
            skipped += 1
            # print(f'Skipped: {os.path.relpath(script_path, base)} - {msg}')
    
    print(f'\n=== Summary ===')
    print(f'Modified: {modified}')
    print(f'Skipped: {skipped}')
    print(f'Total: {modified + skipped}')


if __name__ == '__main__':
    main()
