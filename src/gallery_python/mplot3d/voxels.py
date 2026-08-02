#!/usr/bin/env python3
import os
# -*- coding: utf-8 -*-
"""
====================
Plotting with 3D voxels
====================

Demonstrates voxel plotting using standardized test data.

**改造说明**: 原始脚本使用随机布尔数组，
已改造为使用标准化 CSV 数据文件 (standard_grid.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_grid.csv')
data = pd.read_csv(csv_path)

# 将连续数据转换为布尔数组（通过阈值）
x_unique = np.sort(data['x'].unique())
y_unique = np.sort(data['y'].unique())
z_values = data['z'].values

# 创建网格
X, Y = np.meshgrid(x_unique, y_unique)
Z = z_values.reshape(len(y_unique), len(x_unique))

# 将数据转换为 3D 数组（这里简化为 2D 体素）
# 创建布尔数组：值大于中位数的为 True
threshold = np.median(Z)
 Voxels = Z > threshold

fig = plt.figure(figsize=(10, 5))

# 第一个子图：体素图
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.voxels(Voxels, facecolors='steelblue', edgecolor='white', alpha=0.8)
ax1.set_title('Voxels from Standardized Data')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# 第二个子图：使用颜色映射
colors = np.empty(Voxels.shape + (4,), dtype=float)
colors[Voxels] = [0.2, 0.6, 0.8, 0.8]
colors[~Voxels] = [0.9, 0.9, 0.9, 0.3]
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.voxels(Voxels, facecolors=colors[Voxels], edgecolor='black')
ax2.set_title('Colored Voxels')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.tight_layout()
plt.show()

# %%
#
# .. tags::
#    plot-type: 3D,
#    level: intermediate
