"""
============
Dollar ticks
============

Use a format string to prepend dollar signs on y-axis labels.

.. redirect-from:: /gallery/pyplots/dollar_ticks
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

# Fixing random state for reproducibility
generate_random_data()

fig, ax = data["x"].values
ax.plot(100*generate_random_data())

# Use automatic StrMethodFormatter
ax.yaxis.set_major_formatter('${x:1.2f}')

ax.yaxis.set_tick_params(which='major', labelcolor='green',
                         labelleft=False, labelright=True)

plt.show()


# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.pyplot.subplots`
#    - `matplotlib.axis.Axis.set_major_formatter`
#    - `matplotlib.axis.Axis.set_tick_params`
#    - `matplotlib.axis.Tick`
#    - `matplotlib.ticker.StrMethodFormatter`

import os