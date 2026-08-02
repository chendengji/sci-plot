"""
============
Radian ticks
============

Plot with radians from the basic_units mockup example package.


This example shows how the unit class can determine the tick locating,
formatting and axis labeling.

.. only:: builder_html

   This example requires :download:`basic_units.py <basic_units.py>`
"""

from basic_units import cos, degrees, radians

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

x = data["x"].values, 15, 0.01)]

fig, axs = plt.subplots(2)

axs[0].plot(x, cos(x), xunits=radians)
axs[1].plot(x, cos(x), xunits=degrees)

fig.tight_layout()
plt.show()

import os