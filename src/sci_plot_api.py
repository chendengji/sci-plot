#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sci-plot 统一API - Claude Code 调用入口

用法:
    from sci_plot_api import plot_chart, list_charts, list_styles, read_data, auto_detect_columns

    df = read_data("data.csv")
    plot_chart(df, "bar", x_col="group", y_col="value", style="nature")
"""

import os
import sys
import importlib
import inspect
from datetime import datetime

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import scienceplots

from config import FIGS_DIR


# ==================== 中文字体配置 ====================

# 尝试注册中文字体，避免 scienceplots 的 STIX 字体无法显示中文
_CJK_FONTS = [
    'Microsoft YaHei',        # Windows
    'SimHei',                 # Windows
    'WenQuanYi Micro Hei',    # Linux
    'PingFang SC',            # macOS
    'Noto Sans CJK SC',       # Linux
]
for _fname in _CJK_FONTS:
    try:
        _fp = fm.findfont(_fname, fallback_to_default=False)
        _CJK_FONT = _fname
        break
    except Exception:
        _CJK_FONT = None
else:
    _CJK_FONT = None


def _setup_cjk_font():
    """配置中文字体回退，解决 scienceplots 下中文乱码。"""
    if _CJK_FONT:
        plt.rcParams['font.family'] = 'sans-serif'
        # 将 CJK 字体加入 font.sans-serif 列表首位
        seen = [_CJK_FONT]
        for f in plt.rcParams['font.sans-serif']:
            if f not in seen:
                seen.append(f)
        plt.rcParams['font.sans-serif'] = seen
        # 修复负号显示
        plt.rcParams['axes.unicode_minus'] = False


# ==================== 图表模块注册表 ====================

# 格式: 'chart_type': ('module_path', 'category')
CHART_REGISTRY = {
    # -- basic (xy_series: x_col, y_col, group_col) --
    'bar':        ('charts.basic.bar', 'basic'),
    'line':       ('charts.basic.line', 'basic'),
    'scatter':    ('charts.basic.scatter', 'basic'),
    'stem':       ('charts.basic.stem', 'stats'),
    'stairs':     ('charts.basic.stairs', 'stats'),
    'stackplot':  ('charts.basic.stackplot', 'basic'),
    'fill_between': ('charts.basic.fill_between', 'basic'),
    # -- stats (paired/distribution data) --
    'boxplot':    ('charts.stats.boxplot', 'stats'),
    'violin':     ('charts.stats.violin', 'stats'),
    'hist':       ('charts.stats.histogram', 'stats'),
    'ecdf':       ('charts.stats.ecdf', 'stats'),
    'pie':        ('charts.stats.pie', 'stats'),
    'errorbar':   ('charts.stats.errorbar', 'stats'),
    'hexbin':     ('charts.stats.hexbin', 'stats'),
    'hist2d':     ('charts.stats.hist2d', 'stats'),
    'eventplot':  ('charts.stats.eventplot', 'stats'),
    # -- arrays (gridded data: x, y, z) --
    'contour':    ('charts.arrays.contour', 'arrays'),
    'contourf':   ('charts.arrays.contourf', 'arrays'),
    'pcolormesh': ('charts.arrays.pcolormesh', 'arrays'),
    'imshow':     ('charts.arrays.imshow', 'arrays'),
    'quiver':     ('charts.arrays.quiver', 'arrays'),
    'streamplot': ('charts.arrays.streamplot', 'arrays'),
    'barbs':      ('charts.arrays.barbs', 'arrays'),
    # -- plot3d (3D data: x, y, z) --
    'plot3d':     ('charts.plot3d.plot3d', 'plot3d'),
    'scatter3d':  ('charts.plot3d.scatter3d', 'plot3d'),
    'surface3d':  ('charts.plot3d.surface3d', 'plot3d'),
    'wire3d':     ('charts.plot3d.wire3d', 'plot3d'),
    'bar3d':      ('charts.plot3d.bar3d', 'plot3d'),
    'stem3d':     ('charts.plot3d.stem3d', 'plot3d'),
    'voxels':     ('charts.plot3d.voxels', 'plot3d'),
    'trisurf3d':  ('charts.plot3d.trisurf3d', 'plot3d'),
    'quiver3d':   ('charts.plot3d.quiver3d', 'plot3d'),
    'fill_between3d': ('charts.plot3d.fill_between3d', 'plot3d'),
    # -- unstructured (irregular x, y, z) --
    'tricontour':   ('charts.unstructured.tricontour', 'unstructured'),
    'tricontourf':  ('charts.unstructured.tricontourf', 'unstructured'),
    'tripcolor':    ('charts.unstructured.tripcolor', 'unstructured'),
    'triplot':      ('charts.unstructured.triplot', 'unstructured'),
}

# 图表类型 → 数据类型映射（用于数据预处理）
CHART_DATA_TYPE = {
    # basic / stats → paired
    'bar': 'paired', 'stem': 'paired', 'stairs': 'paired',
    'stackplot': 'paired',
    'fill_between': 'paired',
    'boxplot': 'paired', 'violin': 'paired', 'hist': 'paired',
    'ecdf': 'paired', 'pie': 'paired', 'errorbar': 'paired',
    'eventplot': 'paired',
    'hexbin': 'paired', 'hist2d': 'paired',
    # xy_series (x_col, y_col, group_col)
    'line': 'xy_series', 'scatter': 'xy_series',
    # arrays → gridded
    'contour': 'gridded', 'contourf': 'gridded', 'pcolormesh': 'gridded',
    'imshow': 'gridded', 'quiver': 'gridded', 'streamplot': 'gridded',
    'barbs': 'gridded',
    # plot3d → 3d_volume
    'plot3d': '3d_volume', 'scatter3d': '3d_volume', 'surface3d': '3d_volume',
    'wire3d': '3d_volume', 'bar3d': '3d_volume', 'stem3d': '3d_volume',
    'voxels': '3d_volume', 'trisurf3d': '3d_volume', 'quiver3d': '3d_volume',
    'fill_between3d': '3d_volume',
    # unstructured → irregular
    'tricontour': 'irregular', 'tricontourf': 'irregular',
    'tripcolor': 'irregular', 'triplot': 'irregular',
}

# 3D 图表列表（需要 projection='3d'）
CHARTS_3D = {'plot3d', 'scatter3d', 'surface3d', 'wire3d', 'bar3d',
             'stem3d', 'voxels', 'trisurf3d', 'quiver3d'}

# 可用样式
AVAILABLE_STYLES = ['science', 'nature', 'ieee', 'ieeetran', 'grid']


# ==================== 核心 API ====================

def _import_chart_module(chart_type):
    """动态导入图表模块。"""
    if chart_type not in CHART_REGISTRY:
        raise ValueError(f"Unknown chart type: {chart_type}. "
                         f"Available: {list(CHART_REGISTRY.keys())}")
    module_path, _ = CHART_REGISTRY[chart_type]
    return importlib.import_module(module_path, package='src')


def _preprocess_data(df, chart_type, timestamp, **kwargs):
    """
    根据图表类型对数据进行标准化预处理。

    调用 process_data.py 的对应函数，确保数据：
    - 只保留需要的列
    - 去除空值
    - 按需排序
    - 保存到 data/ 目录
    """
    # 延迟导入，避免循环依赖
    from process_data import (
        process_paired_data, process_xy_series_data,
        process_distribution_data, process_gridded_data,
        process_irregular_data, process_3d_data
    )

    data_type = CHART_DATA_TYPE.get(chart_type, 'paired')

    if data_type == 'paired':
        x_col = kwargs.get('x_col')
        y_col = kwargs.get('y_col')
        df_proc, _, _ = process_paired_data(df, x_col, y_col, timestamp)
        return df_proc

    elif data_type == 'xy_series':
        x_col = kwargs.get('x_col')
        y_col = kwargs.get('y_col')
        group_col = kwargs.get('group_col', None)
        df_proc, _ = process_xy_series_data(df, x_col, y_col, group_col, timestamp)
        return df_proc

    elif data_type == 'distribution':
        value_col = kwargs.get('value_col', kwargs.get('y_col'))
        label_col = kwargs.get('label_col', kwargs.get('x_col'))
        if label_col and label_col not in df.columns:
            label_col = None
        df_proc, _ = process_distribution_data(df, value_col, label_col, timestamp)
        return df_proc

    elif data_type == 'gridded':
        # 网格数据预处理：保留 x,y,z 列，去空值
        x_col = kwargs.get('x_col')
        y_col = kwargs.get('y_col')
        z_col = kwargs.get('z_col')
        if all(c in df.columns for c in [x_col, y_col, z_col]):
            df_proc = df[[x_col, y_col, z_col]].dropna()
        else:
            df_proc = df
        return df_proc

    elif data_type == 'irregular':
        x_col = kwargs.get('x_col')
        y_col = kwargs.get('y_col')
        z_col = kwargs.get('z_col')
        if all(c in df.columns for c in [x_col, y_col, z_col]):
            df_proc = df[[x_col, y_col, z_col]].dropna()
        else:
            df_proc = df
        return df_proc

    elif data_type == '3d_volume':
        x_col = kwargs.get('x_col')
        y_col = kwargs.get('y_col')
        z_col = kwargs.get('z_col')
        cols = [c for c in [x_col, y_col, z_col] if c and c in df.columns]
        if cols:
            df_proc = df[cols].dropna()
        else:
            df_proc = df
        return df_proc

    return df


def plot_chart(df, chart_type, **kwargs):
    """
    统一绘图接口。

    参数
    ----
    df : pd.DataFrame
        原始数据（会自动进行标准化预处理）
    chart_type : str
        图表类型名（如 'bar', 'violin', 'surface3d', 'xy_line'）
    **kwargs :
        x_col, y_col, z_col, u_col, v_col, w_col, c_col : 列映射
        group_col : str, xy_series 类型的分组列
        style : str, 样式名 (默认 'science')
        title : str, 图表标题
        figsize : tuple, 图片尺寸 (默认 (5, 4))
        dpi : int, 输出 DPI (默认 300)

    返回
    ----
    str: 保存的图片路径
    """
    style = kwargs.pop('style', 'nature')
    title = kwargs.pop('title', None)
    figsize = kwargs.pop('figsize', (5, 4))
    dpi = kwargs.pop('dpi', 300)

    # 1. 数据预处理（标准化），每次调用生成独立时间戳
    _timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    df_proc = _preprocess_data(df, chart_type, _timestamp, **kwargs)

    # 2. 设置样式 + 中文字体
    plt.style.use([style, 'no-latex'])
    plt.rcParams['figure.dpi'] = dpi
    _setup_cjk_font()

    # 3. 创建 Figure (3D 图表需要特殊处理)
    if chart_type in CHARTS_3D:
        fig, ax = plt.subplots(figsize=figsize, subplot_kw={'projection': '3d'})
    else:
        fig, ax = plt.subplots(figsize=figsize)

    # 4. 导入并调用图表模块
    module = _import_chart_module(chart_type)
    if title:
        kwargs['title'] = title
    module.plot(fig, ax, df_proc, **kwargs)

    # 5. 保存
    plt.tight_layout()
    os.makedirs(FIGS_DIR, exist_ok=True)
    fig_filename = f'fig_{chart_type}_{_timestamp}.png'
    fig_path = os.path.join(FIGS_DIR, fig_filename)
    fig.savefig(fig_path, dpi=dpi, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)

    return fig_path


def list_charts(category=None):
    """
    列出可用图表类型。

    参数
    ----
    category : str or None
        筛选分类: 'basic', 'stats', 'arrays', 'plot3d', 'unstructured'
        为 None 时返回全部

    返回
    ----
    dict: {chart_type: category}
    """
    if category:
        return {k: v for k, (_, v) in CHART_REGISTRY.items() if v == category}
    return {k: v for k, (_, v) in CHART_REGISTRY.items()}


def list_styles():
    """列出可用样式。"""
    return AVAILABLE_STYLES.copy()


def read_data(filepath):
    """
    读取任意格式数据文件。

    支持 CSV, Excel, TXT, DAT 等格式。
    """
    import pandas as pd
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.csv':
        return pd.read_csv(filepath)
    elif ext in ('.xlsx', '.xls'):
        return pd.read_excel(filepath)
    else:
        return pd.read_csv(filepath, sep=None, engine='python')


def auto_detect_columns(df):
    """
    自动分析 DataFrame 各列的数据类型。

    返回
    ----
    dict: {'numeric': [...], 'categorical': [...], 'other': [...]}
    """
    import pandas as pd
    result = {'numeric': [], 'categorical': [], 'other': []}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            result['numeric'].append(col)
        elif pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col]):
            if df[col].nunique() < df[col].shape[0] * 0.5:
                result['categorical'].append(col)
            else:
                result['other'].append(col)
        else:
            result['other'].append(col)
    return result


def recommend_charts(df):
    """
    根据数据推荐合适的图表类型。

    返回
    ----
    list: [(chart_type, explanation), ...]
    """
    cols = auto_detect_columns(df)
    n_cat = len(cols['categorical'])
    n_num = len(cols['numeric'])

    recs = []
    if n_cat >= 1 and n_num >= 1:
        recs.append(('bar', '分组柱状图'))
        recs.append(('boxplot', '箱线图'))
        recs.append(('violin', '小提琴图'))
        recs.append(('hist', '直方图'))

    if n_num >= 2:
        recs.append(('line', '连续x-y折线图'))
        recs.append(('scatter', '连续x-y散点图'))

    if n_num >= 3:
        recs.append(('scatter3d', '3D散点图'))
        recs.append(('plot3d', '3D折线图'))

    return recs


# ==================== 快捷函数 ====================

def quick_plot(filepath, chart_type, **kwargs):
    """一键读取 + 绘图。"""
    df = read_data(filepath)
    return plot_chart(df, chart_type, **kwargs)


if __name__ == '__main__':
    # 命令行快速测试
    import argparse
    parser = argparse.ArgumentParser(description='sci-plot API quick test')
    parser.add_argument('--input', '-i', required=True, help='Input data file')
    parser.add_argument('--chart', '-ch', required=True, help='Chart type')
    parser.add_argument('--xcol', default='group', help='X column')
    parser.add_argument('--ycol', default='value', help='Y column')
    parser.add_argument('--style', '-s', default='science', help='Style')
    args = parser.parse_args()

    path = quick_plot(args.input, args.chart,
                      x_col=args.xcol, y_col=args.ycol, style=args.style)
    print(f'[OK] Saved: {path}')