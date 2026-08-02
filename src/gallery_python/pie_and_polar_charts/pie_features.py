#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==========
Pie charts
==========

Demo of plotting a pie chart using standardized test data.

**改造说明**: 原始脚本使用硬编码的标签和尺寸数据，
已改造为使用标准化 CSV 数据文件 (standard_categorized.csv)。
"""

# %%
# Label slices
# ------------
#
# Plot a pie chart of categories and label the slices.

import matplotlib.pyplot as plt
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_categorized.csv'
data = pd.read_csv(csv_path)

# 计算各组的平均值作为饼图数据
group_means = data.groupby('category')['value'].mean()
labels = group_means.index.tolist()
sizes = group_means.values.tolist()

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])
ax.set_title('Pie Chart from Standardized Data')

# %%
# Auto-label slices
# -----------------
#
# Pass a function or format string to *autopct* to label slices.

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#9b59b6', '#1abc9c', '#e67e22', '#34495e'])
ax.set_title('Pie Chart with Auto Labels')

# %%
# Color slices
# ------------
#
# Pass a list of colors to *colors* to set the color of each slice.

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels,
       colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown'])
ax.set_title('Pie Chart with Custom Colors')

# %%
# Explode, shade, and rotate slices
# ---------------------------------
#
# * offsetting a slice using *explode*
# * add a drop-shadow using *shadow*
# * custom start angle using *startangle*

explode = (0, 0.1, 0, 0)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90, colors=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])
ax.set_title('Exploded Pie Chart')
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`
#
# .. tags::
#
#    plot-type: pie
#    level: beginner
