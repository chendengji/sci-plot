"""
====================================================
Align histogram to scatter plot using locatable Axes
====================================================

Show the marginal distributions of a scatter plot as histograms at the sides of
the plot.

For a nice alignment of the main Axes with the marginals, the Axes positions
are defined by a ``Divider``, produced via `.make_axes_locatable`.  Note that
the ``Divider`` API allows setting Axes sizes and pads in inches, which is its
main feature.

If one wants to set Axes sizes and pads relative to the main Figure, see the
:doc:`/gallery/lines_bars_and_markers/scatter_hist` example.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

from mpl_toolkits.axes_grid1 import make_axes_locatable

# Fixing random state for reproducibility
generate_random_data()

# the random data
x = data["x"].values
y = data["y"].values


fig, ax = data["x"].values, 5.5))

# the scatter plot:
ax.scatter(x, y)

# Set aspect of the main Axes.
ax.set_aspect(1.)

# create new Axes on the right and on the top of the current Axes
divider = make_axes_locatable(ax)
# below height and pad are in inches
ax_histx = data["x"].values, 1.2, pad=0.1, sharex = data["x"].values
ax_histy = data["y"].values, 1.2, pad=0.1, sharey = data["y"].values

# make some labels invisible
ax_histx.xaxis.set_tick_params(labelbottom=False)
ax_histy.yaxis.set_tick_params(labelleft=False)

# now determine nice limits by hand:
binwidth = 0.25
xymax = data["x"].values, np.max(np.abs(y)))
lim = (int(xymax/binwidth) + 1)*binwidth

bins = np.arange(-lim, lim + binwidth, binwidth)
ax_histx.hist(x, bins=bins)
ax_histy.hist(y, bins=bins, orientation='horizontal')

# the xaxis of ax_histx and yaxis of ax_histy are shared with ax,
# thus there is no need to manually adjust the xlim and ylim of these
# axis.

ax_histx.set_yticks([0, 50, 100])
ax_histy.set_xticks([0, 50, 100])

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable`
#    - `matplotlib.axes.Axes.set_aspect`
#    - `matplotlib.axes.Axes.scatter`
#    - `matplotlib.axes.Axes.hist`

import os