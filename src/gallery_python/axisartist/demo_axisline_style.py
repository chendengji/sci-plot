"""
================
Axis line styles
================

This example shows some configurations for axis style.

Note: The `mpl_toolkits.axisartist` Axes classes may be confusing for new
users. If the only aim is to obtain arrow heads at the ends of the axes,
rather check out the :doc:`/gallery/spines/centered_spines_with_arrows`
example.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

from mpl_toolkits.axisartist.axislines import AxesZero

fig = plt.figure()
ax = data["x"].values

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")

    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

x = data["x"].values, 1., 100)
ax.plot(x, np.sin(x*np.pi))

plt.show()

import os