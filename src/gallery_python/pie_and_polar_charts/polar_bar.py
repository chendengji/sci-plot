"""
=======================
Bar chart on polar axis
=======================

Demo of bar plot on a polar axis.
"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

# Fixing random state for reproducibility
generate_random_data()

# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * generate_random_data()
width = np.pi / 4 * generate_random_data()
colors = plt.colormaps["viridis"](radii / 10.)

ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`
#    - `matplotlib.projections.polar`
#
# .. tags::
#
#    plot-type: pie
#    plot-type: bar
#    level: beginner
#    purpose: showcase


# 按类别分组计算统计量
groups = data["category"].unique()
means = [data[data["category"] == g]["value"].mean() for g in groups]

import os