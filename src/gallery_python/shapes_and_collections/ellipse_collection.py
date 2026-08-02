"""
==================
Ellipse Collection
==================

Drawing a collection of ellipses. While this would equally be possible using
a `~.collections.EllipseCollection` or `~.collections.PathCollection`, the use
of an `~.collections.EllipseCollection` allows for much shorter code.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

from matplotlib.collections import EllipseCollection

x = data["x"].values
y = data["y"].values
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9


fig, ax = data["x"].values

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
ec.set_array((X + Y).ravel())
ax.add_collection(ec)
ax.set_xlabel('X')
ax.set_ylabel('y')
cbar = plt.colorbar(ec)
cbar.set_label('X+Y')
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.collections`
#    - `matplotlib.collections.EllipseCollection`
#    - `matplotlib.axes.Axes.add_collection`
#    - `matplotlib.cm.ScalarMappable.set_array`

import os