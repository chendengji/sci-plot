#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============
3D quiver plot
==============

Demonstrates plotting directional arrows at points on a 3D meshgrid
using standardized test data.

**改造说明**: 原始脚本使用 np.meshgrid 和三角函数生成向量场，
已改造为使用标准化 CSV 数据文件 (standard_vector.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_vector.csv'
data = pd.read_csv(csv_path)

x = data['x']
y = data['y']
z = np.zeros_like(x)  # 3D 中 z 坐标
u = data['u']
v = data['v']
w = np.zeros_like(u)  # 3D 中 w 分量

ax = plt.figure().add_subplot(projection='3d')

# 绘制 3D 箭头
ax.quiver(x, y, z, u, v, w, length=0.15, normalize=False)

ax.set_title('3D Quiver Plot from Standardized Vector Data')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()


# %%
# .. tags::
#    plot-type: 3D,
#    level: beginner
