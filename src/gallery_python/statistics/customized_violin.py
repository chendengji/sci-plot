#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================
Customized violinplot
===================

Demonstrates customization of violin plots using standardized test data.

**改造说明**: 原始脚本使用 np.random.normal() 生成假数据，
已改造为使用标准化 CSV 数据文件 (standard_categorized.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.offsetbox import AnnotationBbox, FrozenImageBox
from matplotlib.cbook import get_sample_data

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_categorized.csv')
data = pd.read_csv(csv_path)

group_data = [data[data['category'] == cat]['value'].values for cat in data['category'].unique()]
group_names = data['category'].unique().tolist()

fig, ax = plt.subplots()

parts = ax.violinplot(group_data, showmeans=True, showmedians=True)

# Customize colors
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i % len(colors)])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians', 'cmeans'):
    vp = parts[partname]
    vp.set_edgecolor('black')
    vp.set_linewidth(1)

ax.set_xticks(range(1, len(group_data) + 1))
ax.set_xticklabels(group_names)
ax.set_title('Customized Violin Plot with Standardized Data')
ax.set_ylabel('Value')

plt.show()

# %%
#
# .. tags:: plot-type: violin, domain: statistics

import os