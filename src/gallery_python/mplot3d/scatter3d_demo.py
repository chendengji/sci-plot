#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================
3D Scatter Plot
================

Demonstrates plotting a 3D scatter plot using standardized test data.

**改造说明**: 原始脚本使用 np.random.rand() 生成随机数据，
已改造为使用标准化 CSV 数据文件 (standard_3d.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tests', 'data', 'standard_3d.csv')
data = pd.read_csv(csv_path)

x = data['x']
y = data['y']
z = data['z']
categories = data['category']

fig = plt.figure(figsize=(12, 5))

# 第一个子图：按颜色分类
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
scatter1 = ax1.scatter(x, y, z, c=categories.map({'A': 'red', 'B': 'green', 'C': 'blue'}),
                       s=50, alpha=0.7, edgecolors='black')
ax1.set_title('3D Scatter: Colored by Category')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
fig.colorbar(scatter1, ax=ax1, shrink=0.5, aspect=10, label='Category')

# 第二个子图：按数值着色
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
scatter2 = ax2.scatter(x, y, z, c=z, cmap='viridis', s=50, alpha=0.7, edgecolors='black')
ax2.set_title('3D Scatter: Colored by Z Value')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
fig.colorbar(scatter2, ax=ax2, shrink=0.5, aspect=10, label='Z Value')

plt.tight_layout()
plt.show()


# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.pyplot.scatter`
#    - `mpl_toolkits.mplot3d`
#    - `matplotlib.figure.Figure.colorbar`
#
# .. tags::
#
#    plot-type: 3D scatter
#    level: beginner

import os