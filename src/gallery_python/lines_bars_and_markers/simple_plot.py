#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
======
Simple
======

Demonstrate the basic attributes of plot() using standardized data.

**改造说明**: 原始脚本使用 np.random.rand() 生成随机数据，
已改造为使用标准化 CSV 数据文件 (standard_xy.csv)。
"""
import matplotlib.pyplot as plt
import pandas as pd

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
x = data['x']
y = data['y']

fig, ax = plt.subplots()
ax.plot(x, y, 'o-', markersize=5, linewidth=2, markerfacecolor='white', markeredgecolor='blue')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Simple Plot with Standardized Data')
ax.grid(True, alpha=0.3)

plt.show()

import os