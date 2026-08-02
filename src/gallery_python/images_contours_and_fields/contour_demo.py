#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============
Contour Demo
============

Illustrate simple contour plotting using standardized test data.

**改造说明**: 原始脚本使用 np.exp() 生成高斯分布数据，
已改造为使用标准化 CSV 数据文件 (standard_grid.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_grid.csv'
data = pd.read_csv(csv_path)

# 将长格式数据转换为网格格式
x_unique = np.sort(data['x'].unique())
y_unique = np.sort(data['y'].unique())
X, Y = np.meshgrid(x_unique, y_unique)
Z = data['z'].values.reshape(len(y_unique), len(x_unique))

# %%
# Create a simple contour plot with labels using default colors.

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simple Contour Plot with Standardized Data')

# %%
# Contour labels can be placed manually by providing list of positions.

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
# 手动选择几个标注位置
manual_locations = []
if len(X) > 2 and len(Y) > 2:
    manual_locations = [(X[1, 1], Y[1, 1]), (X[-2, 1], Y[-2, 1]), (X[1, -1], Y[1, -1])]
ax.clabel(CS, fontsize=10, manual=manual_locations)
ax.set_title('Labels at Selected Locations')

# %%
# You can force all the contours to be the same color.

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6, colors='k')
ax.clabel(CS, fontsize=9)
ax.set_title('Single Color Contours')

# %%
# You can use a colormap to specify the colors.

fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', origin='lower',
               cmap="viridis", extent=[x_unique.min(), x_unique.max(), y_unique.min(), y_unique.max()])
levels = np.linspace(Z.min(), Z.max(), 10)
CS = ax.contour(Z, levels, origin='lower', cmap='viridis',
                linewidths=2, extent=[x_unique.min(), x_unique.max(), y_unique.min(), y_unique.max()])

ax.clabel(CS, levels[::2], fmt='%1.2f', fontsize=10)
ax.set_title('Contours with Colorbar')

fig.colorbar(im, ax=ax, shrink=0.8)
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`
#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`
#    - `matplotlib.axes.Axes.clabel` / `matplotlib.pyplot.clabel`
#
# .. tags::
#
#    plot-type: contour
#    level: beginner
