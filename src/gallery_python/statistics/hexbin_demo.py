#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================
Hexagonal binned plot
=====================

`~.Axes.hexbin` is a 2D histogram plot, in which the bins are hexagons and
the color represents the number of data points within each bin.

**改造说明**: 原始脚本使用 np.random.standard_normal() 生成随机数据，
已改造为使用标准化 CSV 数据文件 (standard_xy.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)

x = data['x']
y = data['y']

xlim = x.min(), x.max()
ylim = y.min(), y.max()

fig, (ax0, ax1) = plt.subplots(ncols=2, sharey=True, figsize=(9, 4))

hb = ax0.hexbin(x, y, gridsize=20, cmap='inferno')
ax0.set(xlim=xlim, ylim=ylim)
ax0.set_title("Hexagon Binning with Standardized Data")
cb = fig.colorbar(hb, ax=ax0, label='counts')

hb = ax1.hexbin(x, y, gridsize=20, bins='log', cmap='inferno')
ax1.set(xlim=xlim, ylim=ylim)
ax1.set_title("With Log Color Scale")
cb = fig.colorbar(hb, ax=ax1, label='counts')

plt.show()

# %%
#
# .. tags:: plot-type: histogram, plot-type: hexbin, domain: statistics
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.hexbin` / `matplotlib.pyplot.hexbin`
