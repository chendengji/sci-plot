#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCI绘图主流程 - 基于官方示例代码

用法:
    python sci_plot.py --input data.csv --dtype paired --chart bar --style science
    python sci_plot.py --input data.xlsx --columns x=group,y=value --chart violin --style nature
"""

import os
import sys
import argparse

import pandas as pd

# 先把 src/ 加入路径，使平铺导入（from config import ...）在脚本模式下可用
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import DATA_DIR, FIGS_DIR, TIMESTAMP
from sci_plot_api import plot_chart, list_charts, read_data, auto_detect_columns, recommend_charts
from process_data import DATA_TYPES


def select_interactive(options, prompt, default=0):
    """交互式选择。"""
    print()
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    choice = input(f"\n{prompt} [default: {default + 1}]: ").strip()
    idx = int(choice) - 1 if choice else default
    return options[idx] if 0 <= idx < len(options) else options[default]


def main():
    parser = argparse.ArgumentParser(description='SCI Plot Tool')
    parser.add_argument('--input', '-i', required=True, help='Input data file')
    parser.add_argument('--dtype', '-d', default='paired',
                        choices=list(DATA_TYPES.keys()),
                        help='Data type: paired, distribution, gridded, irregular, 3d_volume')
    parser.add_argument('--columns', '-c', help='Column mappings (x=col1,y=col2,...)')
    parser.add_argument('--chart', '-ch', help='Chart type')
    parser.add_argument('--style', '-s', default='nature',
                        help=f'Plot style: science, nature, ieee, ieeetran, grid')
    parser.add_argument('--interactive', '-it', action='store_true',
                        help='Interactive mode')
    args = parser.parse_args()

    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(FIGS_DIR, exist_ok=True)

    print("=" * 60)
    print("  SCI Plot Tool")
    print(f"  Session: {TIMESTAMP}")
    print("=" * 60)

    # 1. 读取数据
    df = read_data(args.input)
    print(f"\n[Loaded] {args.input} ({df.shape[0]} rows x {df.shape[1]} cols)")
    print(f"Columns: {list(df.columns)}")

    # 交互模式：自动检测 + 引导
    if args.interactive:
        print("\n--- Column Analysis ---")
        col_info = auto_detect_columns(df)
        print(f"  Numeric: {col_info['numeric']}")
        print(f"  Categorical: {col_info['categorical']}")

        # 推荐图表
        recs = recommend_charts(df)
        if recs:
            print(f"\nRecommended charts:")
            for c, desc in recs[:6]:
                print(f"  - {c} ({desc})")

        # 选择图表
        all_charts = list(list_charts().keys())
        args.chart = select_interactive(all_charts, "Select chart type")

        # 选择样式
        from sci_plot_api import list_styles
        args.style = select_interactive(list_styles(), "Select style")

        # 列映射
        if not args.columns:
            if col_info['categorical'] and col_info['numeric']:
                default_x = col_info['categorical'][0]
                default_y = col_info['numeric'][0]
                x = input(f"X column (group) [{default_x}]: ").strip() or default_x
                y = input(f"Y column (value) [{default_y}]: ").strip() or default_y
                args.columns = f"x={x},y={y}"

    # 2. 解析列映射（CLI 短名 x/y/z/group → API 的 x_col/y_col/... ）
    _COL_ALIASES = {'x': 'x_col', 'y': 'y_col', 'z': 'z_col',
                    'group': 'group_col', 'u': 'u_col', 'v': 'v_col',
                    'w': 'w_col', 'c': 'c_col', 'value': 'y_col'}
    columns = {}
    if args.columns:
        for pair in args.columns.split(','):
            key, val = pair.split('=')
            key = _COL_ALIASES.get(key.strip(), key.strip())
            columns[key] = val.strip()

    print(f"\n[Chart] {args.chart}")
    print(f"[Style] {args.style}")

    # 3. 绘图
    try:
        kwargs = {'style': args.style}
        kwargs.update(columns)

        fig_path = plot_chart(df, args.chart, **kwargs)

        print(f"\n{'=' * 60}")
        print(f"  [OK] Figure saved: {fig_path}")
        print(f"{'=' * 60}")

    except Exception as e:
        print(f"\n[Error] {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())