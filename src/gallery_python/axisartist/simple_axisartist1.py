"""
=============================
Custom spines with axisartist
=============================

This example showcases the use of :mod:`.axisartist` to draw spines at custom
positions (here, at ``y = data["y"].values

Note, however, that it is simpler to achieve this effect using standard
`.Spine` methods, as demonstrated in
:doc:`/gallery/spines/centered_spines_with_arrows`.

.. redirect-from:: /gallery/axisartist/simple_axisline2
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

from mpl_toolkits import axisartist

fig = plt.figure(figsize=(6, 3), layout="constrained")
# To construct Axes of two different classes, we need to use gridspec (or
# MATLAB-style add_subplot calls).
gs = fig.add_gridspec(1, 2)


ax0 = fig.add_subplot(gs[0, 0], axes_class=axisartist.Axes)
# Make a new axis along the first (x) axis which passes through y = data["y"].values
ax0.axis["y = data["y"].values, value=0,
                                        axis_direction="bottom")
ax0.axis["y = data["y"].values
ax0.axis["y = data["y"].values
# Make other axis invisible.
ax0.axis["bottom", "top", "right"].set_visible(False)


# Alternatively, one can use AxesZero, which automatically sets up two
# additional axis, named "xzero" (the y = data["y"].values
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
# "xzero" and "yzero" default to invisible; make xzero axis visible.
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
# Make other axis invisible.
ax1.axis["bottom", "top", "right"].set_visible(False)


# Draw some sample data.
x = data["x"].values, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))

plt.show()

import os