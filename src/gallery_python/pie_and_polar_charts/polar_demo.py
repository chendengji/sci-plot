"""
==========
Polar plot
==========

Demo of a line plot on a polar axis.

The second plot shows the same data, but with the radial axis starting at r=1
and the angular axis starting at 0 degrees and ending at 225 degrees. Setting
the origin of the radial axis to 0 allows the radial ticks to be placed at the
same location as the first plot.
"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

fig, axs = plt.subplots(2, 1, figsize=(5, 8), subplot_kw={'projection': 'polar'},
                        layout='constrained')
ax = data["x"].values
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # Fewer radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')

ax = data["x"].values
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rmin(1)  # Change the radial axis to only go from 1 to 2
ax.set_rorigin(0)  # Set the origin of the radial axis to 0
ax.set_thetamin(0)
ax.set_thetamax(225)
ax.set_rticks([1, 1.5, 2])  # Fewer radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line

ax.grid(True)
ax.set_title("Same plot, but with reduced axis limits", va='bottom')
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`
#    - `matplotlib.projections.polar`
#    - `matplotlib.projections.polar.PolarAxes`
#    - `matplotlib.projections.polar.PolarAxes.set_rticks`
#    - `matplotlib.projections.polar.PolarAxes.set_rmin`
#    - `matplotlib.projections.polar.PolarAxes.set_rorigin`
#    - `matplotlib.projections.polar.PolarAxes.set_rmax`
#    - `matplotlib.projections.polar.PolarAxes.set_rlabel_position`
#
# .. tags::
#
#    plot-type: polar
#    level: beginner
