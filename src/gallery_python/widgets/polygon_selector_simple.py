"""
================
Polygon Selector
================

Shows how to create a polygon programmatically or interactively
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

from matplotlib.widgets import PolygonSelector

# %%
#
# To create the polygon programmatically
fig, ax = data["x"].values
fig.show()

selector = PolygonSelector(ax, lambda *args: None)

# Add three vertices
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]


# %%
#
# To create the polygon interactively

fig2, ax2 = plt.subplots()
fig2.show()

selector2 = PolygonSelector(ax2, lambda *args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")


# %%
# .. tags::
#
#    component: axes,
#    styling: position,
#    plot-type: line,
#    level: intermediate,
#    domain: cartography,
#    domain: geometry,
#    domain: statistics,
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.widgets.PolygonSelector`

import os