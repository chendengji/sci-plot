#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==================
Streamplot Demo
==================

Demonstrates streamplot using standardized vector field data.

**改造说明**: 原始脚本使用 np.meshgrid 和三角函数生成向量场，
已改造为使用标准化 CSV 数据文件 (standard_vector.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_vector.csv'
data = pd.read_csv(csv_path)

# 准备网格数据
x_unique = np.sort(data['x'].unique())
y_unique = np.sort(data['y'].unique())
X, Y = np.meshgrid(x_unique, y_unique)
U = data['u'].values.reshape(len(y_unique), len(x_unique))
V = data['v'].values.reshape(len(y_unique), len(x_unique))

fig, ax = plt.subplots()
ax.streamplot(X, Y, U, V, color='steelblue', linewidth=1, density=1.5)
ax.set_title('Streamplot from Standardized Vector Data')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# %%
# .. tags::
#
#    plot-type: streamplot
#    level: beginner

import os