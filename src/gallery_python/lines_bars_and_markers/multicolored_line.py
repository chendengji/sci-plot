#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============
Colored line
=============

Demonstrates plotting a line with varying color using standardized test data.

**改造说明**: 原始脚本使用 np.sin() 和 np.cos() 生成数据，
已改造为使用标准化 CSV 数据文件 (standard_xy.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.collections import LineCollection

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
x = data['x'].values
y = data['y'].values

# 计算颜色值（基于 x 的位置）
color_values = (x - x.min()) / (x.max() - x.min())

# 创建线段
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# 创建 LineCollection
lc = LineCollection(segments, cmap='viridis', array=color_values)
lc.set_linewidth(3)

fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.set_title('Colored Line from Standardized Data')
ax.set_xlabel('x')
ax.set_ylabel('y')

fig.colorbar(lc, ax=ax, label='Color Value')
plt.show()

# %%
#
# .. tags::
#
#    styling: color
#    plot-type: line
#    level: intermediate

import os