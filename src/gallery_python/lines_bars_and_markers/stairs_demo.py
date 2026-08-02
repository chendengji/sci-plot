#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================================
Basic usage of matplotlib.pyplot.stairs
=====================================

Stairs plots data as a line that only changes value at specified x positions.

**改造说明**: 原始脚本使用随机数据，
已改造为使用标准化 CSV 数据文件 (standard_xy_simple.csv)。
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy_simple.csv'
data = pd.read_csv(csv_path)
x = data['x'].values
y = data['y'].values

# 重新采样用于阶梯图
steps = 20
x_steps = np.linspace(x.min(), x.max(), steps)
y_steps = np.interp(x_steps, x, y)

fig, axes = plt.subplots(nrows=3, figsize=(5, 6))

# Default: step = 'pre'
axes[0].stairs(y_steps, x_steps)
axes[0].set_title("Default: step='pre'")

# step = 'post'
axes[1].stairs(y_steps, x_steps, baseline=-2.5, label='baseline=-2.5')
axes[1].axhline(0, color='grey', ls='--', alpha=0.5)
axes[1].set_title("step='post' with baseline")

# step = 'mid'
axes[2].stairs(y_steps, x_steps, baseline=0, label='baseline=0')
axes[2].axhline(0, color='grey', ls='--', alpha=0.5)
axes[2].set_title("step='mid' with baseline")

for ax in axes:
    ax.legend()
    ax.set_xlim(x_steps.min(), x_steps.max())

fig.tight_layout()
plt.show()

# %%
# .. tags::
#    plot-type: stairs
#    level: beginner

import os