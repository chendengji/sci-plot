#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================
3D Triangle Surface
================

Demonstrates 3D triangle surface plotting using standardized test data.

**改造说明**: 原始脚本使用随机数据，
已改造为使用标准化 CSV 数据文件 (standard_grid.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_grid.csv'
data = pd.read_csv(csv_path)

# 使用三角剖分
x = data['x'].values
y = data['y'].values
z = data['z'].values

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none', alpha=0.8)

ax.set_title('3D Triangular Surface from Standardized Data')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

# %%
# .. tags::
#    plot-type: 3D,
#    level: intermediate
