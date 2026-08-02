"""
===============
Filled contours
===============

`.Axes3D.contourf` differs from `.Axes3D.contour` in that it creates filled
contours, i.e. a discrete number of colours are used to shade the domain.

This is like a `.Axes.contourf` plot in 2D except that the shaded region
corresponding to the level c is graphed on the plane ``z=c``.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

from mpl_toolkits.mplot3d import axes3d

ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.contourf(X, Y, Z, cmap="coolwarm")

plt.show()

# %%
# .. tags::
#    plot-type: 3D,
#    level: beginner


# 将长格式数据转换为网格格式
x_unique = np.sort(data["x"].unique())
y_unique = np.sort(data["y"].unique())
X, Y = np.meshgrid(x_unique, y_unique)
Z = data["z"].values.reshape(len(y_unique), len(x_unique))

import os