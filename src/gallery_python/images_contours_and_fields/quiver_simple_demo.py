"""
==================
Quiver Simple Demo
==================

A simple example of a `~.axes.Axes.quiver` plot with a `~.axes.Axes.quiverkey`.

For more advanced options refer to
:doc:`/gallery/images_contours_and_fields/quiver_demo`.
"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.quiver` / `matplotlib.pyplot.quiver`
#    - `matplotlib.axes.Axes.quiverkey` / `matplotlib.pyplot.quiverkey`


# 向量场数据
X = data["x"].values.reshape(int(len(data)**0.5), int(len(data)**0.5))
Y = data["y"].values.reshape(int(len(data)**0.5), int(len(data)**0.5))
U = data["u"].values.reshape(int(len(data)**0.5), int(len(data)**0.5))
V = data["v"].values.reshape(int(len(data)**0.5), int(len(data)**0.5))

import os