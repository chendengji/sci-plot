"""
======
Cursor
======

"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

from matplotlib.widgets import Cursor

# Fixing random state for reproducibility
generate_random_data()

fig, ax = data["x"].values, 6))

x, y = data["y"].values
ax.plot(x, y, 'o')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Set useblit=True on most backends for enhanced performance.
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.widgets.Cursor`
