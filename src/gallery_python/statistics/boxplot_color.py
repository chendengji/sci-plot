"""
=================================
Box plots with custom fill colors
=================================

To color each box of a box plot individually:

1) use the keyword argument ``patch_artist=True`` to create filled boxes.
2) loop through the created boxes and adapt their color.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

generate_random_data()
fruit_weights = [
    generate_random_data(),
    generate_random_data(),
    generate_random_data(),
]
labels = ['peaches', 'oranges', 'tomatoes']
colors = ['peachpuff', 'orange', 'tomato']

fig, ax = data["x"].values
ax.set_ylabel('fruit weight (g)')

bplot = ax.boxplot(fruit_weights,
                   patch_artist=True,  # fill with color
                   tick_labels=labels)  # will be used to label x-ticks

# fill with colors
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

# %%
#
# .. tags:: styling: color, domain: statistics, plot-type: boxplot
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.boxplot` / `matplotlib.pyplot.boxplot`

import os