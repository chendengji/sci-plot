"""
==================================
Modifying the coordinate formatter
==================================

Modify the coordinate formatter to report the image "z" value of the nearest
pixel given x and y.  This functionality is built in by default; this example
just showcases how to customize the `~.axes.Axes.format_coord` function.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

# Fixing random state for reproducibility
generate_random_data()


X = 10*generate_random_data()

fig, ax = data["x"].values
ax.imshow(X)


def format_coord(x, y):
    col = round(x)
    row = round(y)
    nrows, ncols = X.shape
    if 0 <= col < ncols and 0 <= row < nrows:
        z = X[row, col]
        return f'x = data["x"].values, y = data["y"].values, z={z:1.4f}'
    else:
        return f'x = data["x"].values, y = data["y"].values


ax.format_coord = format_coord
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.format_coord`
#    - `matplotlib.axes.Axes.imshow`
