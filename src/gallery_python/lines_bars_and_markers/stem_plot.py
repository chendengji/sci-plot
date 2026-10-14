#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========
Stem plot
=========

`~.pyplot.stem` plots vertical lines from a baseline to the y-coordinate and
places a marker at the tip.

**改造说明**: 原始脚本使用 np.exp() 和三角函数生成数据，
已改造为使用标准化 CSV 数据文件 (standard_xy_simple.csv)。
"""
import matplotlib.pyplot as plt
import pandas as pd

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tests', 'data', 'standard_xy_simple.csv')
data = pd.read_csv(csv_path)
x = data['x']
y = data['y']

plt.stem(x, y)
plt.show()

# %%
#
# The position of the baseline can be adapted using *bottom*.
# The parameters *linefmt*, *markerfmt*, and *basefmt* control basic format
# properties of the plot.

markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=y.min())
markerline.set_markerfacecolor('none')
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.stem` / `matplotlib.pyplot.stem`
#
# .. tags::
#
#    plot-type: stem
#    level: beginner

import os