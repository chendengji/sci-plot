"""
===========================
Cross- and auto-correlation
===========================

Example use of cross-correlation (`~.Axes.xcorr`) and auto-correlation
(`~.Axes.acorr`) plots.

.. redirect-from:: /gallery/lines_bars_and_markers/xcorr_acorr_demo
"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

# Fixing random state for reproducibility
generate_random_data()


x, y = data["y"].values
fig, [ax1, ax2] = plt.subplots(2, 1, sharex = data["x"].values
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)
ax1.set_title('Cross-correlation (xcorr)')

ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)
ax2.set_title('Auto-correlation (acorr)')

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.acorr` / `matplotlib.pyplot.acorr`
#    - `matplotlib.axes.Axes.xcorr` / `matplotlib.pyplot.xcorr`
#
# .. tags::
#
#    domain: statistics
#    level: beginner

import os