#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==================
Violin plot basics
==================

Violin plots are similar to histograms and box plots in that they show
an abstract representation of the probability distribution of the
sample. Rather than showing counts of data points that fall into bins
or order statistics, violin plots use kernel density estimation (KDE) to
compute an empirical distribution of the sample.

**改造说明**: 原始脚本使用 np.random.normal() 生成假数据，
已改造为使用标准化 CSV 数据文件 (standard_categorized.csv)。
"""

import matplotlib.pyplot as plt
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_categorized.csv'
data = pd.read_csv(csv_path)

# 按组分离数据
group_data = [data[data['category'] == cat]['value'].values for cat in data['category'].unique()]
group_names = data['category'].unique().tolist()

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(12, 6))

# 基本小提琴图
parts = axs[0, 0].violinplot(group_data, showmeans=True, showextrema=True)
axs[0, 0].set_title('Basic Violin Plot')
axs[0, 0].set_xticks(range(1, len(group_data) + 1))
axs[0, 0].set_xticklabels(group_names)

# 显示中位数
for pc in parts['bodies']:
    pc.set_facecolor('lightblue')
    pc.set_alpha(0.7)
for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians'):
    vp = parts[partname]
    vp.set_edgecolor('black')
    vp.set_linewidth(1)

parts = axs[0, 1].violinplot(group_data, showmeans=True, showmedians=True)
axs[0, 1].set_title('With Medians')
axs[0, 1].set_xticks(range(1, len(group_data) + 1))
axs[0, 1].set_xticklabels(group_names)

for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians'):
    vp = parts[partname]
    vp.set_edgecolor('black')
    vp.set_linewidth(1)

# 自定义带宽
parts = axs[0, 2].violinplot(group_data, bw_method=0.1, showmeans=True)
axs[0, 2].set_title('Bandwidth=0.1')
axs[0, 2].set_xticks(range(1, len(group_data) + 1))
axs[0, 2].set_xticklabels(group_names)

for pc in parts['bodies']:
    pc.set_facecolor('lightcoral')
    pc.set_alpha(0.7)

parts = axs[1, 0].violinplot(group_data, bw_method='silverman', showmeans=True)
axs[1, 0].set_title("Silverman's bandwidth")
axs[1, 0].set_xticks(range(1, len(group_data) + 1))
axs[1, 0].set_xticklabels(group_names)

for pc in parts['bodies']:
    pc.set_facecolor('lightgreen')
    pc.set_alpha(0.7)

# 水平小提琴图
parts = axs[1, 1].violinplot(group_data, orientation='horizontal', showmeans=True)
axs[1, 1].set_title('Horizontal Violin')
axs[1, 1].set_yticks(range(1, len(group_data) + 1))
axs[1, 1].set_yticklabels(group_names)

for pc in parts['bodies']:
    pc.set_facecolor('plum')
    pc.set_alpha(0.7)

# 只显示部分统计量
parts = axs[1, 2].violinplot(group_data, showmeans=False, showextrema=False, showmedians=True)
axs[1, 2].set_title('Medians Only')
axs[1, 2].set_xticks(range(1, len(group_data) + 1))
axs[1, 2].set_xticklabels(group_names)

fig.suptitle('Violin Plots with Standardized Data', fontsize=14)
fig.tight_layout()
plt.show()

# %%
#
# .. tags:: plot-type: violin, domain: statistics
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.violinplot` / `matplotlib.pyplot.violinplot`
