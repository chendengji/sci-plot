#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==========
Histograms
==========

How to plot histograms with Matplotlib using standardized test data.

**改造说明**: 原始脚本使用 np.random.default_rng() 生成随机正态分布数据，
已改造为使用标准化 CSV 数据文件 (standard_categorized.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# 读取标准化测试数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_categorized.csv'
data = pd.read_csv(csv_path)

# 提取不同组的数据
dist1 = data[data['category'] == 'Control']['value'].values
dist2 = data[data['category'] == 'Treated_A']['value'].values

# %%
# Generate data and plot a simple histogram
# -----------------------------------------

n_bins = 15

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(dist1, bins=n_bins, color='steelblue', edgecolor='black', alpha=0.7)
axs[1].hist(dist2, bins=n_bins, color='coral', edgecolor='black', alpha=0.7)

axs[0].set_title('Control Group')
axs[1].set_title('Treated A Group')

plt.show()


# %%
# Updating histogram colors
# -------------------------

fig, axs = plt.subplots(1, 2, tight_layout=True)

# N is the count in each bin, bins is the lower-limit of the bin
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# We'll color code by height, but you could use any scalar
fracs = N / N.max()

# we need to normalize the data to 0..1 for the full range of the colormap
norm = colors.Normalize(fracs.min(), fracs.max())

# Now, we'll loop through our objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.colormaps["viridis"](norm(thisfrac))
    thispatch.set_facecolor(color)

# We can also normalize our inputs by the total number of counts
axs[1].hist(dist2, bins=n_bins, density=True)

# Now we format the y-axis to display percentage
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()


# %%
# Customizing your histogram
# --------------------------

fig, axs = plt.subplots(2, 1, figsize=(5, 8), tight_layout=True)

# We can increase the number of bins on each axis
axs[0].hist(dist1, bins=20, color='mediumseagreen', alpha=0.7, edgecolor='black')
axs[0].set_title('Control Group - 20 Bins')

# As well as define normalization of the colors
axs[1].hist(dist2, bins=15, density=True, color='orchid', alpha=0.7, edgecolor='black')
axs[1].set_title('Treated A Group - Normalized')

plt.show()

# %%
#
# .. tags::
#
#    plot-type: histogram
#    domain: statistics
#    styling: color,
#    component: normalization
#    component: patch
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.hist` / `matplotlib.pyplot.hist`
#    - `matplotlib.ticker.PercentFormatter`
