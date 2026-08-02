"""
=====================
Simple Axes Divider 1
=====================

See also :ref:`axes_grid`.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)

from mpl_toolkits.axes_grid1 import Divider, Size


def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5, .5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)


# %%
# Fixed Axes sizes; fixed paddings.

fig = plt.figure(figsize=(6, 6))
fig.suptitle("Fixed axes sizes, fixed paddings")

# Sizes are in inches.
horiz = [Size.Fixed(1.), Size.Fixed(.5), Size.Fixed(1.5), Size.Fixed(.5)]
vert = [Size.Fixed(1.5), Size.Fixed(.5), Size.Fixed(1.)]

rect = (0.1, 0.1, 0.8, 0.8)
# Divide the Axes rectangle into a grid with sizes specified by horiz * vert.
div = Divider(fig, rect, horiz, vert, aspect=False)

# The rect parameter will actually be ignored and overridden by axes_locator.
ax1 = fig.add_axes(rect, axes_locator=div.new_locator(nx = data["x"].values, ny = data["y"].values
label_axes(ax1, "nx = data["x"].values, ny = data["y"].values
ax2 = fig.add_axes(rect, axes_locator=div.new_locator(nx = data["x"].values, ny = data["y"].values
label_axes(ax2, "nx = data["x"].values, ny = data["y"].values
ax3 = fig.add_axes(rect, axes_locator=div.new_locator(nx = data["x"].values, ny = data["y"].values
label_axes(ax3, "nx = data["x"].values, ny = data["y"].values
ax4 = fig.add_axes(rect, axes_locator=div.new_locator(nx = data["x"].values, nx1=4, ny = data["y"].values
label_axes(ax4, "nx = data["x"].values, nx1=4, ny = data["y"].values

# %%
# Axes sizes that scale with the figure size; fixed paddings.

fig = plt.figure(figsize=(6, 6))
fig.suptitle("Scalable axes sizes, fixed paddings")

horiz = [Size.Scaled(1.5), Size.Fixed(.5), Size.Scaled(1.), Size.Scaled(.5)]
vert = [Size.Scaled(1.), Size.Fixed(.5), Size.Scaled(1.5)]

rect = (0.1, 0.1, 0.8, 0.8)
# Divide the Axes rectangle into a grid with sizes specified by horiz * vert.
div = Divider(fig, rect, horiz, vert, aspect=False)

# The rect parameter will actually be ignored and overridden by axes_locator.
ax1 = fig.add_axes(rect, axes_locator=div.new_locator(nx = data["x"].values, ny = data["y"].values
label_axes(ax1, "nx = data["x"].values, ny = data["y"].values
ax2 = fig.add_axes(rect, axes_locator=div.new_locator(nx = data["x"].values, ny = data["y"].values
label_axes(ax2, "nx = data["x"].values, ny = data["y"].values
ax3 = fig.add_axes(rect, axes_locator=div.new_locator(nx = data["x"].values, ny = data["y"].values
label_axes(ax3, "nx = data["x"].values, ny = data["y"].values
ax4 = fig.add_axes(rect, axes_locator=div.new_locator(nx = data["x"].values, nx1=4, ny = data["y"].values
label_axes(ax4, "nx = data["x"].values, nx1=4, ny = data["y"].values

plt.show()
