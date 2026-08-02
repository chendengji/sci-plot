#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=======
3D stem
=======

Demonstration of a stem plot in 3D, which plots vertical lines from a baseline
to the *z*-coordinate and places a marker at the tip.

**改造说明**: 原始脚本使用 np.cos() 和 np.sin() 生成圆形数据，
已改造为使用标准化 CSV 数据文件 (standard_3d.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\references\gallery_python\tests\data\standard_3d.csv'
data = pd.read_csv(csv_path)

x = data['x']
y = data['y']
z = data['z']

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

ax.set_title('3D Stem Plot with Standardized Data')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

# %%
#
# The position of the baseline can be adapted using *bottom*. The parameters
# *linefmt*, *markerfmt*, and *basefmt* control basic format properties of the
# plot.

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=z.min())
markerline.set_markerfacecolor('none')
ax.set_title('3D Stem with Custom Baseline')

plt.show()

# %%
#
# The orientation of the stems and baseline can be changed using *orientation*.

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=z.min(), orientation='x')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Stem (Horizontal)')

plt.show()

# %%
# .. tags::
#    plot-type: 3D, plot-type: specialty,
#    level: beginner
