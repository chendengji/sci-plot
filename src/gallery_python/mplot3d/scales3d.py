"""
================================
Scales on 3D (Log, Symlog, etc.)
================================

Demonstrate how to use non-linear scales such as logarithmic scales on 3D axes.

3D axes support the same axis scales as 2D plots: 'linear', 'log', 'symlog',
'logit', 'asinh', and custom 'function' scales. This example shows a mix of
scales: linear on X, log on Y, and symlog on Z.

For a complete list of built-in scales, see `matplotlib.scale`. For an overview
of scale transformations, see :doc:`/gallery/scales/scales`.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

# A sine chirp with increasing frequency and amplitude
x = np.linspace(0, 1, 400)  # time
y = 10 ** (2 * x)  # frequency, growing exponentially from 1 to 100 Hz
phase = 2 * np.pi * (10 ** (2 * x) - 1) / (2 * np.log(10))
z = np.sin(phase) * x **2 * 10  # amplitude, growing quadratically

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z)

ax.set_xlabel('Time (linear)')
ax.set_ylabel('Frequency, Hz (log)')
ax.set_zlabel('Amplitude (symlog)')

ax.set_yscale('log')
ax.set_zscale('symlog')

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale`
#    - `mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale`
#    - `mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale`
#    - `matplotlib.scale`
#
# .. tags::
#    plot-type: 3D,
#    level: beginner


# 将长格式数据转换为网格格式
x_unique = np.sort(data["x"].unique())
y_unique = np.sort(data["y"].unique())
X, Y = np.meshgrid(x_unique, y_unique)
Z = data["z"].values.reshape(len(y_unique), len(x_unique))

import os