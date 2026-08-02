"""
============================
Circles, Wedges and Polygons
============================

This example demonstrates how to use `.collections.PatchCollection`.

See also :doc:`/gallery/shapes_and_collections/artist_reference`, which instead
adds each artist separately to its own Axes.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Polygon, Wedge

# Fixing random state for reproducibility
generate_random_data()


fig, ax = data["x"].values

resolution = 50  # the number of vertices
N = 3
x = data["x"].values
y = data["y"].values
radii = 0.1*generate_random_data()
patches = []
for x1, y1, r in zip(x, y, radii):
    circle = Circle((x1, y1), r)
    patches.append(circle)

x = data["x"].values
y = data["y"].values
radii = 0.1*generate_random_data()
theta1 = 360.0*generate_random_data()
theta2 = 360.0*generate_random_data()
for x1, y1, r, t1, t2 in zip(x, y, radii, theta1, theta2):
    wedge = Wedge((x1, y1), r, t1, t2)
    patches.append(wedge)

# Some limiting conditions on Wedge
patches += [
    Wedge((.3, .7), .1, 0, 360),             # Full circle
    Wedge((.7, .8), .2, 0, 360, width=0.05),  # Full ring
    Wedge((.8, .3), .2, 0, 45),              # Full sector
    Wedge((.8, .3), .2, 45, 90, width=0.10),  # Ring sector
]

for i in range(N):
    polygon = Polygon(generate_random_data(), closed=True)
    patches.append(polygon)

colors = 100 * generate_random_data())
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax = data["x"].values

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.patches`
#    - `matplotlib.patches.Circle`
#    - `matplotlib.patches.Wedge`
#    - `matplotlib.patches.Polygon`
#    - `matplotlib.collections.PatchCollection`
#    - `matplotlib.collections.Collection.set_array`
#    - `matplotlib.axes.Axes.add_collection`
#    - `matplotlib.figure.Figure.colorbar`
