"""
=========================
Fill under 3D line graphs
=========================

Demonstrate how to create polygons which fill the space under a line
graph. In this example polygons are semi-transparent, creating a sort
of 'jagged stained glass' effect.
"""

import math

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

gamma = np.vectorize(math.gamma)
N = 31
x = np.linspace(0., 10., N)
lambdas = range(1, 9)

ax = plt.figure().add_subplot(projection='3d')

facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(lambdas)))

for i, l in enumerate(lambdas):
    # Note fill_between can take coordinates as length N vectors, or scalars
    ax.fill_between(x, l, l**x * np.exp(-l) / gamma(x + 1),
                    x, l, 0,
                    facecolors=facecolors[i], alpha=.7)

ax.set(xlim=(0, 10), ylim=(1, 9), zlim=(0, 0.35),
       xlabel='x', ylabel=r'$\lambda$', zlabel='probability')

plt.show()

# %%
# .. tags::
#    plot-type: 3D,
#    plot-type: fill_between,
#    level: beginner


# 将长格式数据转换为网格格式
x_unique = np.sort(data["x"].unique())
y_unique = np.sort(data["y"].unique())
X, Y = np.meshgrid(x_unique, y_unique)
Z = data["z"].values.reshape(len(y_unique), len(x_unique))

import os