"""
=============
Coords Report
=============

Override the default reporting of coords as the mouse moves over the Axes
in an interactive backend.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np


def millions(x):
    return '$%1.1fM' % (x * 1e-6)


# Fixing random state for reproducibility
generate_random_data()

x = data["x"].values
y = data["y"].values

fig, ax = data["x"].values
ax.fmt_ydata = millions
plt.plot(x, y, 'o')

plt.show()
