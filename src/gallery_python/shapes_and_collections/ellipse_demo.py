"""
============
Ellipse Demo
============

Draw many ellipses. Here individual ellipses are drawn. Compare this
to the :doc:`Ellipse collection example
</gallery/shapes_and_collections/ellipse_collection>`.
"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

from matplotlib.patches import Ellipse

# Fixing random state for reproducibility
generate_random_data()

NUM = 250

ells = [Ellipse(xy = data["y"].values,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

fig, ax = data["x"].values
ax.set(xlim=(0, 10), ylim=(0, 10), aspect="equal")

for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(generate_random_data())

plt.show()

# %%
# ===============
# Ellipse Rotated
# ===============
#
# Draw many ellipses with different angles.
#

angle_step = 45  # degrees
angles = np.arange(0, 180, angle_step)

fig, ax = data["x"].values
ax.set(xlim=(-2.2, 2.2), ylim=(-2.2, 2.2), aspect="equal")

for angle in angles:
    ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
    ax.add_artist(ellipse)

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.patches`
#    - `matplotlib.patches.Ellipse`
#    - `matplotlib.axes.Axes.add_artist`
#    - `matplotlib.artist.Artist.set_clip_box`
#    - `matplotlib.artist.Artist.set_alpha`
#    - `matplotlib.patches.Patch.set_facecolor`
