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

try:
    from .config import FIGS_DIR          # 包模式: from src.sci_plot_api import ...
except ImportError:
    from config import FIGS_DIR           # 平铺模式: sys.path.insert(0,'src')


# ==================== 中文字体配置 ====================
#
# 优先使用系统自带的中文字体（黑体 SimHei、宋体 SimSun、微软雅黑 等）。
#
# 已知问题：matplotlib 默认只扫描 Linux 字体目录，不扫描 WSL2 挂载的
#   /mnt/c/Windows/Fonts，因此 Windows 自带的 SimHei/SimSun 即便存在，
#   findfont 也找不到（旧实现只按名字 findfont，所以在 WSL2 下中文乱码）。
# 修复：主动用 addfont() 注册候选字体文件，再按优先级解析字体名。
# 跨平台：Windows 原生 / WSL2 挂载点 / Linux / macOS 字体目录都尝试。

import glob as _glob

# 候选 CJK 字体目录（跨平台）
_CJK_FONT_DIRS = [
    "/mnt/c/Windows/Fonts",          # WSL2 → Windows C 盘
    "/mnt/d/Windows/Fonts",          # WSL2 → Windows D 盘
    "C:/Windows/Fonts",               # Windows 原生
    "/usr/share/fonts",               # Linux
    "/usr/local/share/fonts",
    os.path.expanduser("~/.fonts"),
    os.path.expanduser("~/.local/share/fonts"),
    "/System/Library/Fonts",          # macOS
    "/Library/Fonts",
]

# 候选 CJK 字体文件名（黑体/宋体/雅黑 优先）
_CJK_FONT_FILES = [
    "simhei.ttf",        # SimHei 黑体
    "simsun.ttc",        # SimSun 宋体
    "nsimsun.ttf",       # NSimSun 新宋体
    "msyh.ttc",          # Microsoft YaHei 微软雅黑
    "msyhbd.ttc",        # Microsoft YaHei Bold
    "simfang.ttf",       # FangSong 仿宋
    "simkai.ttf",        # KaiTi 楷体
    "STSONG.TTF",        # STSong 华文宋体
    "wqy-zenhei.ttc",    # WenQuanYi Zen Hei
    "wqy-microhei.ttc",  # WenQuanYi Micro Hei
    "NotoSansCJKsc-Regular.otf",
    "NotoSansSC-Regular.otf",
    "SourceHanSansSC-Regular.otf",
    "PingFang.ttc",
]

# 字体名解析优先级：黑体 > 宋体 > 新宋体 > 雅黑 > 仿宋/楷体 > 文泉驿 > Noto > 思源 > 苹方
_CJK_FONT_PRIORITY = [
    "SimHei", "SimSun", "NSimSun", "Microsoft YaHei",
    "FangSong", "KaiTi", "STSong",
    "WenQuanYi Zen Hei", "WenQuanYi Micro Hei",
    "Noto Sans CJK SC", "Noto Sans SC", "Source Han Sans SC", "PingFang SC",
]


def _register_cjk_fonts():
    """扫描候选目录并用 addfont() 注册 CJK 字体文件（WSL2 下必需，仅内存生效）。"""
    for d in _CJK_FONT_DIRS:
        if not os.path.isdir(d):
            continue
        names = list(_CJK_FONT_FILES)
        # glob 兜底：再扫该目录下其他 sim*/msyh*/wqy*/Noto*/SourceHan*/ST* 等
        for pat in ("sim*.tt[fc]", "msyh*.tt[fc]", "wqy*.tt[fc]",
                    "Noto*CJK*", "NotoSansSC*", "SourceHan*",
                    "PingFang*", "ST*.TTF", "*.otc"):
            names += _glob.glob(os.path.join(d, pat))
        seen = set()
        for fname in names:
            p = fname if os.path.isabs(fname) else os.path.join(d, fname)
            if p in seen or not os.path.isfile(p):
                continue
            try:
                fm.fontManager.addfont(p)
                seen.add(p)
            except Exception:
                pass


def _resolve_cjk_font():
    """按优先级返回第一个 matplotlib 可识别的 CJK 字体名。"""
    for name in _CJK_FONT_PRIORITY:
        try:
            fm.findfont(name, fallback_to_default=False)
            return name
        except Exception:
            continue
    return None


# 模块导入时注册一次（仅作用于当前进程，不改动系统字体缓存）
_register_cjk_fonts()
_CJK_FONT = _resolve_cjk_font()


def _setup_cjk_font():
    """配置中文字体回退，解决 scienceplots(STIX) 下中文乱码。

    优先级：黑体(SimHei) > 宋体(SimSun) > 微软雅黑 > 文泉驿 > Noto...
    找不到任何 CJK 字体时不改 rcParams，避免破坏当前样式。
    """
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
    # xy_series (两个数值列 x_col, y_col, 可选 group_col)
    'line': 'xy_series', 'scatter': 'xy_series',
    'hexbin': 'xy_series', 'hist2d': 'xy_series',
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

# 可用样式（scienceplots 实测可用；'ieeetran' 已移除，scienceplots 无此样式会抛 OSError）
AVAILABLE_STYLES = ['science', 'nature', 'ieee', 'grid']


# ==================== 核心 API ====================

def _import_chart_module(chart_type):
    """动态导入图表模块（兼容包模式与平铺模式两种调用方式）。

    包模式(from src.sci_plot_api import): __package__='src' → src.charts.basic.line
    平铺模式(sys.path.insert(0,'src'); from sci_plot_api import): __package__='' → charts.basic.line
    """
    if chart_type not in CHART_REGISTRY:
        raise ValueError(f"Unknown chart type: {chart_type}. "
                         f"Available: {list(CHART_REGISTRY.keys())}")
    module_path, _ = CHART_REGISTRY[chart_type]
    pkg = __package__ or ''
    full = f'{pkg}.{module_path}' if pkg else module_path
    return importlib.import_module(full)


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
    try:
        from .process_data import (
            process_paired_data, process_xy_series_data,
            process_distribution_data, process_gridded_data,
            process_irregular_data, process_3d_data
        )
    except ImportError:
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
            df_proc = df.dropna(subset=[x_col, y_col, z_col])
        else:
            df_proc = df
        return df_proc

    elif data_type == 'irregular':
        x_col = kwargs.get('x_col')
        y_col = kwargs.get('y_col')
        z_col = kwargs.get('z_col')
        if all(c in df.columns for c in [x_col, y_col, z_col]):
            # dropna(subset=) 而非 df[[...]]：当 y_col 与 z_col 同名时避免重名列
            df_proc = df.dropna(subset=[x_col, y_col, z_col])
        else:
            df_proc = df
        return df_proc

    elif data_type == '3d_volume':
        x_col = kwargs.get('x_col')
        y_col = kwargs.get('y_col')
        z_col = kwargs.get('z_col')
        cols = [c for c in [x_col, y_col, z_col] if c and c in df.columns]
        # 用 dropna(subset=...) 而非 df[cols]：当 x_col 与 z_col 同名时
        # df[cols] 会产生重名列、返回 DataFrame，下游 df[x_col] 取到多列
        # 报 shape mismatch。subset 只按列名去空值，保留原结构。
        return df.dropna(subset=cols) if cols else df

    return df


def _apply_typography(figsize=None, fontsize=None):
    """按期刊样式基准同步缩放字号，避免“大图小字”失衡。

    scienceplots 的 nature/science 样式是“figsize + font.size 配套”设计的
    （如 nature: 3.3in 宽 + 7pt 字）。若单独放大 figsize 而不动字号，字会
    相对图极小、留白失衡——本函数负责让两者联动。

    - 都为 None：完全沿用样式自带值（推荐，符合期刊比例）。
    - figsize= 自定义：按 新宽/基准宽 比例同步放大 font.size 等字号。
    - fontsize= 自定义：作为主控钮，覆盖 font.size 并令各元素字号跟随。
    """
    base_w = plt.rcParams['figure.figsize'][0]
    base_font = plt.rcParams['font.size']

    if figsize is not None:
        plt.rcParams['figure.figsize'] = figsize
        scale = figsize[0] / base_w if base_w else 1.0
        new_font = base_font * scale
    else:
        new_font = base_font

    if fontsize is not None:
        new_font = fontsize

    if figsize is not None or fontsize is not None:
        plt.rcParams['font.size'] = new_font
        for k in ('axes.labelsize', 'xtick.labelsize', 'ytick.labelsize',
                  'legend.fontsize'):
            plt.rcParams[k] = new_font
        plt.rcParams['axes.titlesize'] = new_font + 1


def plot_chart(df, chart_type, **kwargs):
    """
    统一绘图接口。

    参数
    ----
    df : pd.DataFrame
        原始数据（会自动进行标准化预处理）
    chart_type : str
        图表类型名（如 'bar', 'violin', 'line', 'scatter', 'surface3d'）
    **kwargs :
        x_col, y_col, z_col, u_col, v_col, w_col, c_col : 列映射
        group_col : str, xy_series 类型的分组列
        style : str, 样式名 (默认 'nature')
        title : str, 图表标题
        figsize : tuple or None, 图片尺寸；None=用样式自带基准（推荐，字号配套）
        fontsize : float or None, 基准字号(pt)；None=用样式自带；给定则作为主控钮
        dpi : int, 输出 DPI (默认 300)
        constrained_layout : bool, 是否启用约束布局 (默认 True；多子图/colorbar/legend 不打架)
        legend_loc : str or None, 图例位置 (如 'best','upper left'；None=默认)
        legend_frame : bool, 是否显示图例边框 (默认 False)

    返回
    ----
    str: 保存的图片路径
    """
    style = kwargs.pop('style', 'nature')
    title = kwargs.pop('title', None)
    figsize = kwargs.pop('figsize', None)
    fontsize = kwargs.pop('fontsize', None)
    dpi = kwargs.pop('dpi', 300)
    legend_loc = kwargs.pop('legend_loc', None)
    legend_frame = kwargs.pop('legend_frame', False)
    use_constrained = kwargs.pop('constrained_layout', True)

    # 1. 数据预处理（标准化），每次调用生成独立时间戳
    _timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    df_proc = _preprocess_data(df, chart_type, _timestamp, **kwargs)

    # 2. 设置样式 + 中文字体 + 字号(与 figsize 联动)
    plt.style.use([style, 'no-latex'])
    plt.rcParams['figure.dpi'] = dpi
    _setup_cjk_font()
    _apply_typography(figsize=figsize, fontsize=fontsize)

    # 3. 创建 Figure（3D 对 constrained_layout 支持有限，走 tight_layout 回退）
    is_3d = chart_type in CHARTS_3D
    if is_3d:
        fig, ax = plt.subplots(figsize=figsize, subplot_kw={'projection': '3d'})
    else:
        layout = 'constrained' if use_constrained else None
        fig, ax = plt.subplots(figsize=figsize, layout=layout)

    # 4. 导入并调用图表模块
    if title:
        kwargs['title'] = title
    module = _import_chart_module(chart_type)
    module.plot(fig, ax, df_proc, **kwargs)

    # 5. 统一图例：默认无边框、位置可配（模块内 ax.legend() 的标签会保留）
    handles, labels = ax.get_legend_handles_labels()
    if labels:
        ax.legend(handles, labels, loc=legend_loc, frameon=legend_frame)

    # 6. 保存
    if not is_3d and use_constrained:
        save_kw = dict(dpi=dpi)  # constrained_layout 已处理布局，不再 tight
    else:
        plt.tight_layout()
        save_kw = dict(dpi=dpi, bbox_inches='tight', pad_inches=0.1)
    os.makedirs(FIGS_DIR, exist_ok=True)
    fig_filename = f'fig_{chart_type}_{_timestamp}.png'
    fig_path = os.path.join(FIGS_DIR, fig_filename)
    fig.savefig(fig_path, **save_kw)
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