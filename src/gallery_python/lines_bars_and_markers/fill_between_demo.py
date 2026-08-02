#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================
Fill the area between two lines
===============================

This example shows how to use fill_between with standardized test data.

**改造说明**: 原始脚本使用 np.sin() 生成正弦波数据，
已改造为使用标准化 CSV 数据文件 (standard_xy.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)

# 分离两组数据
x = data['x'].values
y1 = data[data['group'] == 'Series_A']['y'].values
y2 = data[data['group'] == 'Series_B']['y'].values

# 基本用法
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 8))

ax1.fill_between(x, y1, alpha=0.3, color='steelblue')
ax1.plot(x, y1, 'b-', linewidth=2)
ax1.set_title('fill between y1 and 0')
ax1.set_ylabel('y1')

ax2.fill_between(x, y1, y2, alpha=0.3, color='coral')
ax2.plot(x, y1, 'b-', linewidth=2, label='Series A')
ax2.plot(x, y2, 'r-', linewidth=2, label='Series B')
ax2.set_title('fill between y1 and y2')
ax2.set_ylabel('y')
ax2.legend()

# 使用 where 条件填充
ax3.fill_between(x, y1, alpha=0.3, color='green', where=(y1 > 0))
ax3.plot(x, y1, 'g-', linewidth=2)
ax3.axhline(0, color='black', linestyle='--', alpha=0.5)
ax3.set_title('fill between y1 and 0 (conditional)')
ax3.set_xlabel('x')
ax3.set_ylabel('y1')

fig.tight_layout()
plt.show()


# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.fill_between` / `matplotlib.pyplot.fill_between`
#    - `matplotlib.axes.Axes.get_xaxis_transform`
#
# .. tags::
#
#    styling: conditional
#    plot-type: fill_between
#    level: beginner
#    purpose: showcase
