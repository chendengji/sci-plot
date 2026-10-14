#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================
Parametric curve
================

This example demonstrates plotting a parametric curve in 3D using
standardized test data.

**改造说明**: 原始脚本使用三角函数生成螺旋线数据，
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

ax = plt.figure().add_subplot(projection='3d')

ax.plot(x, y, z, label='3D Line from Standardized Data', linewidth=2)
ax.scatter(x, y, z, color='red', s=30, alpha=0.6)
ax.legend()

ax.set_title('3D Parametric Curve with Standardized Data')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

# %%
# .. tags::
#    plot-type: 3D,
#    level: beginner

import os