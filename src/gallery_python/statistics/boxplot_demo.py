#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========
Boxplots
========

Visualizing boxplots with matplotlib using standardized test data.

**改造说明**: 原始脚本使用 np.random.rand() 生成假数据，
已改造为使用标准化 CSV 数据文件 (standard_categorized.csv)。
"""

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.patches import Polygon

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_categorized.csv')
data = pd.read_csv(csv_path)

# 按组分离数据
group_data = [data[data['category'] == cat]['value'].values for cat in data['category'].unique()]
group_names = data['category'].unique().tolist()

fig, axs = plt.subplots(2, 3, figsize=(12, 8))

# basic plot
axs[0, 0].boxplot(group_data, labels=group_names)
axs[0, 0].set_title('Basic Boxplot')
axs[0, 0].set_ylabel('Value')

# notched plot
axs[0, 1].boxplot(group_data, labels=group_names, notch=True)
axs[0, 1].set_title('Notched Boxplot')
axs[0, 1].set_ylabel('Value')

# change outlier point symbols
axs[0, 2].boxplot(group_data, labels=group_names, sym='gD')
axs[0, 2].set_title('Custom Outlier Symbols')
axs[0, 2].set_ylabel('Value')

# don't show outlier points
axs[1, 0].boxplot(group_data, labels=group_names, sym='')
axs[1, 0].set_title("Don't Show Outliers")
axs[1, 0].set_ylabel('Value')

# horizontal boxes
axs[1, 1].boxplot(group_data, labels=group_names, sym='rs', orientation='horizontal')
axs[1, 1].set_title('Horizontal Boxes')
axs[1, 1].set_xlabel('Value')

# change whisker length
axs[1, 2].boxplot(group_data, labels=group_names, sym='rs', orientation='horizontal', whis=0.75)
axs[1, 2].set_title('Shorter Whiskers')
axs[1, 2].set_xlabel('Value')

fig.tight_layout()
plt.show()

# %%
# 更多分组对比图
# ---------------

fig, ax = plt.subplots(figsize=(10, 6))

bp = ax.boxplot(group_data, patch_artist=True, labels=group_names)

# 设置填充颜色
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# 设置须线和中位线颜色
for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=1.5)
for cap in bp['caps']:
    cap.set(color='black', linewidth=1.5)
for median in bp['medians']:
    median.set(color='black', linewidth=2)

# Add a horizontal grid to the plot
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)

ax.set(
    title='Boxplot of Standardized Data by Category',
    xlabel='Category',
    ylabel='Value'
)

plt.show()

# %%
#
# .. tags:: domain: statistics, plot-type: boxplot
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.boxplot` / `matplotlib.pyplot.boxplot`
#    - `matplotlib.artist.Artist.set` / `matplotlib.pyplot.setp`

import os