"""
==============================================
Mapping marker properties to multivariate data
==============================================

This example shows how to use different properties of markers to plot
multivariate datasets. Here we represent a successful baseball throw as a
smiley face with marker size mapped to the skill of thrower, marker rotation to
the take-off angle, and thrust to the marker color.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

from matplotlib.colors import Normalize
from matplotlib.markers import MarkerStyle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D

SUCCESS_SYMBOLS = [
    TextPath((0, 0), "☹"),
    TextPath((0, 0), "😒"),
    TextPath((0, 0), "☺"),
]

N = 25
generate_random_data()
skills = generate_random_data() * 0.1 + 5
takeoff_angles = generate_random_data()
thrusts = generate_random_data()
successful = generate_random_data()
positions = generate_random_data()) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)

cmap = plt.colormaps["plasma"]
fig, ax = data["x"].values
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap="plasma"),
             ax = data["x"].values, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")

plt.show()

# %%
# .. tags::
#
#    component: marker
#    styling: color,
#    styling: shape
#    level: beginner
#    purpose: fun

import os