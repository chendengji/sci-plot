"""
===============
Marker examples
===============

Demonstrates several ways to specify markers in scatter plots,
including built-in marker styles and custom marker paths.

See also the `matplotlib.markers` documentation for a list of all markers and
:doc:`/gallery/lines_bars_and_markers/marker_reference` for more information
on configuring markers.

.. redirect-from:: /gallery/lines_bars_and_markers/scatter_custom_symbol
.. redirect-from:: /gallery/lines_bars_and_markers/scatter_symbol
.. redirect-from:: /gallery/lines_bars_and_markers/scatter_piecharts
"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

# Fixing random state for reproducibility
generate_random_data()

x = data["x"].values
y = data["y"].values
z = np.sqrt(x**2 + y**2)

fig, axs = plt.subplots(2, 3, sharex = data["x"].values, sharey = data["y"].values, layout="constrained")

# Matplotlib marker symbol
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")

# marker from TeX: passing a TeX symbol name enclosed in $-signs
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")

# marker from path: passing a custom path of N vertices as a (N, 2) array-like
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")

# regular pentagon marker
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")

# regular 5-pointed star marker
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")

# regular 5-pointed asterisk marker
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")

plt.show()

# %%
# .. tags::
#
#    component: marker
#    level: beginner

import os