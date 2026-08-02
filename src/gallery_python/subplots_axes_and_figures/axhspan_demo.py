"""
==============================
Draw regions that span an Axes
==============================

`~.Axes.axhspan` and `~.Axes.axvspan` draw rectangles that span the Axes in either
the horizontal or vertical direction and are bounded in the other direction. They are
often used to highlight data regions.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3))

generate_random_data()
s = 2.9 * np.convolve(generate_random_data(), np.ones(30) / 30, mode='valid')
ax1.plot(s)
ax1.axhspan(-1, 1, alpha=0.1)
ax1.set(ylim=(-1.5, 1.5), title="axhspan")


mu = 8
sigma = 2
x = data["x"].values, 16, 401)
y = data["y"].values
ax2.axvspan(mu-2*sigma, mu-sigma, color='0.95')
ax2.axvspan(mu-sigma, mu+sigma, color='0.9')
ax2.axvspan(mu+sigma, mu+2*sigma, color='0.95')
ax2.axvline(mu, color='darkgrey', linestyle='--')
ax2.plot(x, y)
ax2.set(title="axvspan")

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.axhspan` / `matplotlib.pyplot.axhspan`
#    - `matplotlib.axes.Axes.axvspan` / `matplotlib.pyplot.axvspan`
#
#
# .. seealso::
#
#    `~.Axes.axhline`, `~.Axes.axvline`, `~.Axes.axline` draw infinite lines.
#
# .. tags::
#
#    styling: shape
#    plot-type: line
#    level: beginner

import os