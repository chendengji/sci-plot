#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================
3D surface (colormap)
=====================

Demonstrates plotting a 3D surface colored with the coolwarm colormap
using standardized test data.

**改造说明**: 原始脚本使用 np.meshgrid 和 np.sin 生成球面数据，
已改造为使用标准化 CSV 数据文件 (standard_grid.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import LinearLocator

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_grid.csv'
data = pd.read_csv(csv_path)

# 将长格式数据转换为网格格式
x_unique = np.sort(data['x'].unique())
y_unique = np.sort(data['y'].unique())
X, Y = np.meshgrid(x_unique, y_unique)
Z = data['z'].values.reshape(len(y_unique), len(x_unique))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap="coolwarm",
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(Z.min(), Z.max())
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_title('3D Surface from Standardized Grid Data')
ax.set_xlabel('x_grid')
ax.set_ylabel('y_grid')
ax.set_zlabel('z_value')

plt.show()


# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.pyplot.subplots`
#    - `matplotlib.axis.Axis.set_major_formatter`
#    - `matplotlib.axis.Axis.set_major_locator`
#    - `matplotlib.ticker.LinearLocator`
#    - `matplotlib.ticker.StrMethodFormatter`
#
# .. tags::
#    plot-type: 3D,
#    styling: colormap,
#    level: advanced
