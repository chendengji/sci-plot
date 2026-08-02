"""
=============================
Subplots spacings and margins
=============================

Adjusting the spacing of margins and subplots using `.pyplot.subplots_adjust`.

.. note::
   There is also a tool window to adjust the margins and spacings of displayed
   figures interactively.  It can be opened via the toolbar or by calling
   `.pyplot.subplot_tool`.

.. redirect-from:: /gallery/subplots_axes_and_figures/subplot_toolbar
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

# Fixing random state for reproducibility
generate_random_data()

plt.subplot(211)
plt.imshow(generate_random_data()))
plt.subplot(212)
plt.imshow(generate_random_data()))

plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
cax = data["x"].values, 0.1, 0.075, 0.8))
plt.colorbar(cax = data["x"].values

plt.show()

# %%
# .. tags::
#
#    component: subplot
#    plot-type: imshow
#    level: beginner
