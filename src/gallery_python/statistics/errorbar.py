#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================
Errorbar function
================

Demonstrates basic errorbar plotting using standardized test data.

**改造说明**: 原始脚本使用 np.exp() 生成数据，
已改造为使用标准化 CSV 数据文件 (standard_categorized.csv)。
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_categorized.csv')
data = pd.read_csv(csv_path)

# 计算分组统计
groups = data['category'].unique()
x = np.arange(len(groups))
means = [data[data['category'] == g]['value'].mean() for g in groups]
stds = [data[data['category'] == g]['value'].std() for g in groups]

fig, ax = plt.subplots()
ax.errorbar(x, means, yerr=stds, fmt='o', capsize=5, capthick=2,
           color='steelblue', markersize=8)
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.set_title('Errorbar from Standardized Data')
ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.grid(True, alpha=0.3)

plt.show()

# %%
#
#
# .. tags:: plot-type: errorbar, domain: statistics,
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`

import os