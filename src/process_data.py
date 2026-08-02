#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sci-plot 标准化数据处理脚本
根据用户选择的数据类型进行相应处理
"""

import os
import numpy as np
import pandas as pd
from config import DATA_DIR

# ==================== 数据类型定义 ====================

DATA_TYPES = {
    'paired': {
        'name': '成对数据 (Paired Data)',
        'description': '分组数据，每行一个观测值',
        'columns': ['group', 'value'],
        'charts': ['bar', 'boxplot', 'violin', 'hist', 'ecdf', 'pie',
                   'stem', 'errorbar', 'stairs', 'stackplot', 'fill_between',
                   'eventplot', 'hexbin', 'hist2d'],
        'example': 'group: Control/Treated, value: 测量值'
    },
    'xy_series': {
        'name': '连续XY数据 (XY Series)',
        'description': '两个连续数值列，x-y 关系，可选分组',
        'columns': ['x', 'y', 'group'],
        'charts': ['line', 'scatter'],
        'example': '应力应变曲线、时间序列'
    },
    'distribution': {
        'name': '统计分布 (Distribution)',
        'description': '单变量或多变量分布数据',
        'columns': ['values', 'labels'],
        'charts': ['violin', 'hist', 'ecdf', 'pie', 'stem', 'boxplot'],
        'example': '多组数据用于分布可视化'
    },
    'gridded': {
        'name': '网格数据 (Gridded Data)',
        'description': '规则网格上的二维/三维数据',
        'columns': ['X', 'Y', 'Z'],
        'charts': ['pcolormesh', 'contour', 'contourf', 'imshow',
                   'quiver', 'streamplot', 'barbs'],
        'example': '温度场、高度图等'
    },
    'irregular': {
        'name': '非规则网格数据 (Irregular Grid)',
        'description': '不规则分布的二维数据',
        'columns': ['x', 'y', 'z'],
        'charts': ['tricontour', 'tricontourf', 'tripcolor', 'triplot'],
        'example': '地理数据、散点插值'
    },
    '3d_volume': {
        'name': '三维/体积数据 (3D & Volume)',
        'description': '三维空间数据或体素数据',
        'columns': ['x', 'y', 'z', 'v'],
        'charts': ['plot3d', 'scatter3d', 'surface3d', 'wire3d', 'bar3d',
                   'stem3d', 'voxels', 'trisurf3d', 'quiver3d', 'fill_between3d'],
        'example': '曲面、体数据'
    }
}


def process_paired_data(df, x_col, y_col, timestamp):
    """处理成对数据"""
    df_clean = df[[x_col, y_col]].dropna()
    df_clean[x_col] = df_clean[x_col].astype(str)
    
    data_filename = f'processed_{timestamp}.csv'
    output_path = os.path.join(DATA_DIR, data_filename)
    df_clean.to_csv(output_path, index=False)
    
    groups = sorted(df_clean[x_col].unique())
    stats = []
    for g in groups:
        subset = df_clean[df_clean[x_col] == g]
        stats.append({
            'group': g,
            'n': len(subset),
            'mean': subset[y_col].mean(),
            'std': subset[y_col].std()
        })
    
    return df_clean, data_filename, stats


def process_xy_series_data(df, x_col, y_col, group_col, timestamp):
    """处理连续XY数据（应力应变曲线、时间序列等）"""
    cols = [x_col, y_col]
    if group_col and group_col in df.columns:
        cols.append(group_col)
    df_clean = df[cols].dropna()
    # 按分组和x排序
    if group_col and group_col in df.columns:
        df_clean = df_clean.sort_values([group_col, x_col])
    else:
        df_clean = df_clean.sort_values(x_col)

    data_filename = f'xyseries_{timestamp}.csv'
    output_path = os.path.join(DATA_DIR, data_filename)
    df_clean.to_csv(output_path, index=False)

    return df_clean, data_filename


def process_distribution_data(df, value_col, label_col, timestamp):
    """处理统计分布数据"""
    df_clean = df[[value_col]].copy()
    if label_col and label_col in df.columns:
        df_clean['label'] = df[label_col].astype(str)
    
    data_filename = f'distribution_{timestamp}.csv'
    output_path = os.path.join(DATA_DIR, data_filename)
    df_clean.to_csv(output_path, index=False)
    
    return df_clean, data_filename


def process_gridded_data(df, x_col, y_col, z_col, timestamp):
    """处理网格数据"""
    x_unique = sorted(df[x_col].unique())
    y_unique = sorted(df[y_col].unique())

    X, Y = np.meshgrid(x_unique, y_unique)
    Z = np.full((len(y_unique), len(x_unique)), np.nan)
    x_to_idx = {v: i for i, v in enumerate(x_unique)}
    y_to_idx = {v: i for i, v in enumerate(y_unique)}
    for _, row in df.iterrows():
        Z[y_to_idx[row[y_col]], x_to_idx[row[x_col]]] = row[z_col]
    
    data_filename = f'gridded_{timestamp}.npz'
    output_path = os.path.join(DATA_DIR, data_filename)
    np.savez(output_path, X=X, Y=Y, Z=Z)
    
    return X, Y, Z, data_filename


def process_irregular_data(df, x_col, y_col, z_col, timestamp):
    """处理非规则网格数据"""
    df_clean = df[[x_col, y_col, z_col]].dropna()
    
    data_filename = f'irregular_{timestamp}.csv'
    output_path = os.path.join(DATA_DIR, data_filename)
    df_clean.to_csv(output_path, index=False)
    
    return df_clean[[x_col, y_col, z_col]].values, data_filename


def process_3d_data(df, x_col, y_col, z_col, v_col, timestamp):
    """处理三维/体积数据"""
    cols = [x_col, y_col, z_col]
    if v_col and v_col in df.columns:
        cols.append(v_col)
    df_clean = df[cols].dropna()
    
    data_filename = f'3d_{timestamp}.csv'
    output_path = os.path.join(DATA_DIR, data_filename)
    df_clean.to_csv(output_path, index=False)
    
    return df_clean, data_filename


def process_data(df, *args, timestamp=None, data_type='paired', v_col=None, group_col=None):
    """
    主处理函数（按 data_type 分派到具体处理函数）。

    参数
    ----
    df : pd.DataFrame
        输入数据
    *args : tuple
        按 data_type 传递：
        - paired: (x_col, y_col)
        - xy_series: (x_col, y_col)
        - distribution: (value_col, label_col/None)
        - gridded: (x_col, y_col, z_col)
        - irregular: (x_col, y_col, z_col)
        - 3d_volume: (x_col, y_col, z_col)
    timestamp : str, optional
        时间戳（用于输出文件名），默认从 config.TIMESTAMP 获取
    data_type : str
        数据类型（paired, xy_series, distribution, gridded, irregular, 3d_volume）
    v_col : str, optional
        3D 数据值列
    group_col : str, optional
        xy_series 分组列
    """
    if timestamp is None:
        from config import TIMESTAMP
        timestamp = TIMESTAMP

    if data_type == 'paired':
        x_col, y_col = args[0], args[1]
        return process_paired_data(df, x_col, y_col, timestamp)
    elif data_type == 'xy_series':
        x_col, y_col = args[0], args[1]
        return process_xy_series_data(df, x_col, y_col, group_col, timestamp)
    elif data_type == 'distribution':
        value_col, label_col = args[0], args[1]
        return process_distribution_data(df, value_col, label_col, timestamp)
    elif data_type == 'gridded':
        x_col, y_col, z_col = args[0], args[1], args[2]
        return process_gridded_data(df, x_col, y_col, z_col, timestamp)
    elif data_type == 'irregular':
        x_col, y_col, z_col = args[0], args[1], args[2]
        return process_irregular_data(df, x_col, y_col, z_col, timestamp)
    elif data_type == '3d_volume':
        x_col, y_col, z_col = args[0], args[1], args[2]
        return process_3d_data(df, x_col, y_col, z_col, v_col, timestamp)
    else:
        raise ValueError(f"Unknown data type: {data_type}")


def get_available_charts(data_type):
    """获取可用图表类型"""
    return DATA_TYPES.get(data_type, DATA_TYPES['paired'])['charts']


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t', required=True, 
                        choices=list(DATA_TYPES.keys()),
                        help='Data type to process')
    parser.add_argument('--input', '-i', required=True, help='Input file')
    parser.add_argument('--columns', '-c', help='Column mappings')
    args = parser.parse_args()
    
    ext = os.path.splitext(args.input)[1].lower()
    if ext == '.csv':
        df = pd.read_csv(args.input)
    elif ext in ['.xlsx', '.xls']:
        df = pd.read_excel(args.input)
    else:
        df = pd.read_csv(args.input, sep=None, engine='python')
    
    columns = {}
    if args.columns:
        for pair in args.columns.split(','):
            key, val = pair.split('=')
            columns[key.strip()] = val.strip()
    
    from config import TIMESTAMP
    result = process_data(df, timestamp=TIMESTAMP, data_type=args.type, **columns)
    print(f"Processed {args.type} data: {result}")
