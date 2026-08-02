#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================
Plot contour (level) curves in 3D
================================

This demonstrates contour curves in 3D using standardized test data.

**改造说明**: 原始脚本使用 axes3d.get_test_data() 生成测试数据，
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

ax = plt.figure().add_subplot(projection='3d')
ax.contour(X, Y, Z, cmap="coolwarm")  # Plot contour curves

ax.set_title('3D Contour from Standardized Grid Data')
ax.set_xlabel('x_grid')
ax.set_ylabel('y_grid')
ax.set_zlabel('z_value')

plt.show()

# %%
# .. tags::
#    plot-type: 3D,
#    level: beginner
