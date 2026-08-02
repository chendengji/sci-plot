#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
Scatter plot with histograms
===========================

Add histograms to the x-axes and y-axes margins of a scatter plot
using standardized test data.

**改造说明**: 原始脚本使用 np.random.randn() 生成随机数据，
已改造为使用标准化 CSV 数据文件 (standard_xy.csv)。
"""

import matplotlib.pyplot as plt
import pandas as pd

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
x = data['x']
y = data['y']


def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y, alpha=0.6, s=30, color='steelblue', edgecolors='black')

    # now determine nice limits by hand:
    binwidth = 0.5
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins, color='lightblue', edgecolor='black')
    ax_histy.hist(y, bins=bins, orientation='horizontal', color='lightcoral', edgecolor='black')

import numpy as np

# Defining the Axes positions using subplot_mosaic
fig, axs = plt.subplot_mosaic([['histx', '.'],
                               ['scatter', 'histy']],
                              figsize=(6, 6),
                              width_ratios=(4, 1), height_ratios=(1, 4),
                              layout='constrained')
scatter_hist(x, y, axs['scatter'], axs['histx'], axs['histy'])
axs['scatter'].set_title('Scatter with Histograms\nfrom Standardized Data')
axs['scatter'].set_xlabel('x')
axs['scatter'].set_ylabel('y')

plt.show()

# %%
#
# .. tags::
#
#    component: axes
#    plot-type: scatter
#    plot-type: histogram
#    level: intermediate

import os