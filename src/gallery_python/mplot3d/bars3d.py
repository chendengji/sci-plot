#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========
3D Bars
========

Demonstrates creating 3D bar charts using standardized test data.

**改造说明**: 原始脚本使用 np.random.rand() 生成随机数据，
已改造为使用标准化 CSV 数据文件 (standard_3d.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_3d.csv'
data = pd.read_csv(csv_path)

# 准备数据
x = data['x']
y = data['y']
z = data['z']

# 创建图形
fig = plt.figure(figsize=(12, 5))

# 第一个子图：基本 3D 柱状图
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# 计算每个位置的柱状图高度（按 x, y 分组）
pivot_table = data.pivot_table(values='z', index='x', columns='y', aggfunc='mean')
x_vals = pivot_table.index.values
y_vals = pivot_table.columns.values
z_vals = pivot_table.values

# 创建柱状图
x_idx = np.arange(len(x_vals))
y_idx = np.arange(len(y_vals))
X, Y = np.meshgrid(x_idx, y_idx)
X = X.flatten()
Y = Y.flatten()
Z = z_vals.flatten()

ax1.bar3d(X, Y, np.zeros_like(Z), 0.5, 0.5, Z, shade=True)
ax1.set_title('3D Bar Chart from Standardized Data')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# 第二个子图：按颜色分类的 3D 柱状图
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# 按类别分组
categories = ['A', 'B', 'C']
colors = ['red', 'green', 'blue']

for cat_idx, cat in enumerate(categories):
    cat_data = data[data['category'] == cat]
    if len(cat_data) > 0:
        x_cat = cat_data['x']
        y_cat = cat_data['y']
        z_cat = cat_data['z']
        
        # 创建柱状图
        ax2.bar3d(x_cat, y_cat, np.zeros_like(z_cat), 0.3, 0.3, z_cat,
                 color=colors[cat_idx], alpha=0.7)

ax2.set_title('3D Bar Chart by Category')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.tight_layout()
plt.show()


# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d`
#    - `matplotlib.pyplot.subplots`
#
# .. tags::
#
#    plot-type: 3D,
#    level: intermediate

import os