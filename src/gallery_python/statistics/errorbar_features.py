#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================
Errorbar visualization
=====================

Demonstrates errorbar plotting using standardized test data.

**改造说明**: 原始脚本使用 np.random.rand() 生成假数据，
已改造为使用标准化 CSV 数据文件 (standard_categorized.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_categorized.csv'
data = pd.read_csv(csv_path)

# 计算各组的均值和标准差
groups = data['category'].unique()
means = [data[data['category'] == g]['value'].mean() for g in groups]
stds = [data[data['category'] == g]['value'].std() for g in groups]
x = np.arange(len(groups))

# 基本误差棒图
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 1. 基本误差棒
axes[0, 0].errorbar(x, means, yerr=stds, fmt='o', capsize=5, capthick=2)
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(groups, rotation=15)
axes[0, 0].set_title('Basic Errorbar')
axes[0, 0].set_ylabel('Value')

# 2. 水平误差棒
axes[0, 1].errorbar(means, x, xerr=stds, fmt='o', capsize=5, capthick=2, color='coral')
axes[0, 1].set_yticks(x)
axes[0, 1].set_yticklabels(groups)
axes[0, 1].set_title('Horizontal Errorbar')
axes[0, 1].set_xlabel('Value')

# 3. 不对称误差棒
yerr_lower = [stds[i] * 0.8 for i in range(len(stds))]
yerr_upper = [stds[i] * 1.2 for i in range(len(stds))]
axes[1, 0].errorbar(x, means, yerr=[yerr_lower, yerr_upper], fmt='s', capsize=3, color='green')
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(groups, rotation=15)
axes[1, 0].set_title('Asymmetric Errorbar')
axes[1, 0].set_ylabel('Value')

# 4. 带标记的误差棒
axes[1, 1].errorbar(x, means, yerr=stds, fmt='D', capsize=8, capthick=2,
                   elinewidth=2, markerfacecolor='white', markeredgecolor='blue', markersize=8)
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(groups, rotation=15)
axes[1, 1].set_title('Styled Errorbar')
axes[1, 1].set_ylabel('Value')

fig.tight_layout()
plt.show()

# %%
#
# .. tags:: plot-type: errorbar
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`
