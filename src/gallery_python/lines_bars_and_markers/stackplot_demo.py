#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
Stackplots with CSV data
===========================

Stackplots draw multiple datasets as vertically stacked areas.

**改造说明**: 原始脚本使用世界人口数据和随机高斯混合数据，
已改造为使用标准化 CSV 数据文件 (standard_xy.csv)。
"""

# %%
# Stackplots
# ----------
#
# Stackplots draw multiple datasets as vertically stacked areas.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据（使用分组数据）
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

# 分离两组数据作为堆叠数据
x = data['x'].values
y1 = data[data['group'] == 'Series_A']['y'].values
y2 = data[data['group'] == 'Series_B']['y'].values

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, labels=['Series A', 'Series B'], alpha=0.8)
ax.legend(loc='upper left')
ax.set_title('Stackplot with Standardized Data')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()

# %%
# Streamgraphs
# ------------
#
# Using the *baseline* parameter, you can turn an ordinary stacked area plot
# with baseline 0 into a stream graph.

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, baseline='wiggle', labels=['Series A', 'Series B'], alpha=0.8)
ax.legend(loc='upper left')
ax.set_title('Streamgraph with Standardized Data')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()

# %%
# .. tags::
#
#    plot-type: stackplot
#    level: intermediate

import os