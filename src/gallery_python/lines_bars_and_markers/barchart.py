#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================
Grouped bar chart with labels
=============================

This example shows how to create a grouped bar chart using standardized test data.

**改造说明**: 原始脚本使用 Penguin 数据集硬编码数据，
已改造为使用标准化 CSV 数据文件 (standard_categorized.csv)。
"""

import matplotlib.pyplot as plt
import pandas as pd

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_categorized.csv')
data = pd.read_csv(csv_path)

# 计算每组的平均值
group_means = data.groupby('category')['value'].mean()
groups = group_means.index.tolist()
means = group_means.values.tolist()

fig, ax = plt.subplots(layout='constrained')

# 绘制分组柱状图
x = range(len(groups))
width = 0.6
bars = ax.bar(x, means, width, color='steelblue', edgecolor='black')

# 在柱子上添加标签
ax.bar_label(bars, padding=3, fmt='%.1f')

# Add some text for labels, title, etc.
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.set_ylabel('Value')
ax.set_title('Bar Chart with Standardized Data')

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`
#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`
#
# .. tags::
#
#    component: label
#    plot-type: bar
#    level: beginner

import os