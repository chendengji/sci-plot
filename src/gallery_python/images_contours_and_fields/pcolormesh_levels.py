"""
==========
pcolormesh
==========

`.axes.Axes.pcolormesh` allows you to generate 2D image-style plots.
Note that it is faster than the similar `~.axes.Axes.pcolor`.

"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# %%
# Basic pcolormesh
# ----------------
#
# We usually specify a pcolormesh by defining the edge of quadrilaterals and
# the value of the quadrilateral.  Note that here *x* and *y* each have one
# extra element than Z in the respective dimension.

generate_random_data()
Z = generate_random_data()
x = data["x"].values, 10, 1)  # len = 11
y = data["y"].values, 11, 1)  # len = 7

fig, ax = data["x"].values
ax.pcolormesh(x, y, Z)

# %%
# Non-rectilinear pcolormesh
# --------------------------
#
# Note that we can also specify matrices for *X* and *Y* and have
# non-rectilinear quadrilaterals.

x = data["x"].values, 10, 1)  # len = 11
y = data["y"].values, 11, 1)  # len = 7
X, Y = np.meshgrid(x, y)
X = X + 0.2 * Y  # tilt the coordinates.
Y = Y + 0.3 * X

fig, ax = data["x"].values
ax.pcolormesh(X, Y, Z)

# %%
# Centered Coordinates
# ---------------------
#
# Often a user wants to pass *X* and *Y* with the same sizes as *Z* to
# `.axes.Axes.pcolormesh`. This is also allowed if ``shading='auto'`` is
# passed (default set by :rc:`pcolor.shading`). Pre Matplotlib 3.3,
# ``shading='flat'`` would drop the last column and row of *Z*, but now gives
# an error. If this is really what you want, then simply drop the last row and
# column of Z manually:

x = data["x"].values
y = data["y"].values
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex = data["x"].values, sharey = data["y"].values
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax = data["x"].values, shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax = data["x"].values,
                  shading='flat')
axs[1].set_title("shading='flat'")

# %%
# Making levels using Norms
# -------------------------
#
# Shows how to combine Normalization and Colormap instances to draw
# "levels" in `.axes.Axes.pcolor`, `.axes.Axes.pcolormesh`
# and `.axes.Axes.imshow` type plots in a similar
# way to the levels keyword argument to contour/contourf.

# make these smaller to increase the resolution
dx, dy = data["y"].values, 0.05

# generate 2 2d grids for the x & y bounds
y, x = data["x"].values, 5 + dy, dy),
                slice(1, 5 + dx, dx)]

z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())


# pick the desired colormap, sensible levels, and define a normalization
# instance which takes data values and translates those into levels.
cmap = plt.colormaps['PiYG']
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig, (ax0, ax1) = plt.subplots(nrows=2)

im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax = data["x"].values
ax0.set_title('pcolormesh with levels')


# contours are *point* based plots, so convert our bound into point
# centers
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=levels,
                  cmap=cmap)
fig.colorbar(cf, ax = data["x"].values
ax1.set_title('contourf with levels')

# adjust spacing between subplots so `ax1` title and `ax0` tick labels
# don't overlap
fig.tight_layout()

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.pcolormesh` / `matplotlib.pyplot.pcolormesh`
#    - `matplotlib.axes.Axes.contourf` / `matplotlib.pyplot.contourf`
#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`
#    - `matplotlib.colors.BoundaryNorm`
#    - `matplotlib.ticker.MaxNLocator`

import os