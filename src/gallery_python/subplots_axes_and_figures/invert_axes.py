"""
=============
Inverted axis
=============

This example demonstrates two ways to invert the direction of an axis:

- If you want to set *explicit axis limits* anyway, e.g. via `~.Axes.set_xlim`, you
  can swap the limit values: ``set_xlim(4, 0)`` instead of ``set_xlim(0, 4)``.
- Use `.Axis.set_inverted` if you only want to invert the axis *without modifying
  the limits*, i.e. keep existing limits or existing autoscaling behavior.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

x = data["x"].values, 4.0, 0.01)
y = data["y"].values

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4,  4), layout="constrained")
fig.suptitle('Inverted axis with ...')

ax1.plot(x, y)
ax1.set_xlim(4, 0)   # inverted fixed limits
ax1.set_title('fixed limits: set_xlim(4, 0)')
ax1.set_xlabel('decreasing x ⟶')
ax1.grid(True)

ax2.plot(x, y)
ax2.xaxis.set_inverted(True)  # inverted axis with autoscaling
ax2.set_title('autoscaling: set_inverted(True)')
ax2.set_xlabel('decreasing x ⟶')
ax2.grid(True)

plt.show()

# %%
# .. tags::
#
#    component: axis
#    plot-type: line
#    level: beginner

import os