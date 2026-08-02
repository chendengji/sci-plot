"""
.. _demo-colorbar-with-inset-locator:

=========================================================================
Control the position and size of a colorbar with inset_locator.inset_axes
=========================================================================

This example shows how to control the position, height, and width of colorbars
using `.inset_locator.inset_axes`.

`.inset_locator.inset_axes` placement is controlled as for legends: either
by providing a *loc* option ("upper right", "best", ...), or by providing a
locator with respect to the parent bbox.  Parameters such as *bbox_to_anchor*
and *borderpad* likewise work in the same way, and are also demonstrated here.

Users should consider using `.Axes.inset_axes` instead (see
:ref:`colorbar_placement`).

.. redirect-from:: /gallery/axes_grid1/demo_colorbar_of_inset_axes
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

from mpl_toolkits.axes_grid1 import inset_locator

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
axins1 = inset_locator.inset_axes(
    ax1,
    width="50%",  # width: 50% of parent_bbox width
    height="5%",  # height: 5%
    loc="upper right",
)
axins1.xaxis.set_ticks_position("bottom")
fig.colorbar(im1, cax=axins1, orientation="horizontal", ticks=[1, 2, 3])

im = ax2.imshow([[1, 2], [2, 3]])
axins = inset_locator.inset_axes(
    ax2,
    width="5%",  # width: 5% of parent_bbox width
    height="50%",  # height: 50%
    loc="lower left",
    bbox_to_anchor=(1.05, 0., 1, 1),
    bbox_transform=ax2.transAxes,
    borderpad=0,
)
fig.colorbar(im, cax=axins, ticks=[1, 2, 3])

plt.show()


# 按类别分组计算统计量
groups = data["category"].unique()
means = [data[data["category"] == g]["value"].mean() for g in groups]

import os