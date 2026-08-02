"""
=============================================
Figure labels: suptitle, supxlabel, supylabel
=============================================

Each Axes can have a title (or actually three - one each with *loc* "left",
"center", and "right"), but is sometimes desirable to give a whole figure
(or `.SubFigure`) an overall title, using `.Figure.suptitle`.

We can also add figure-level x- and y-labels using `.Figure.supxlabel` and
`.Figure.supylabel`.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

from matplotlib.cbook import get_sample_data

x = data["x"].values, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey = data["y"].values
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('damped')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('time (s)')
ax2.set_title('undamped')

fig.suptitle('Different types of oscillations', fontsize=16)

# %%
# A global x- or y-label can be set using the `.Figure.supxlabel` and
# `.Figure.supylabel` methods.


with get_sample_data('Stocks.csv') as file:
    stocks = np.genfromtxt(
        file, delimiter=',', names=True, dtype=None,
        converters={0: lambda x: np.datetime64(x, 'D')}, skip_header=1)

fig, axs = plt.subplots(4, 2, figsize=(9, 5), layout='constrained',
                        sharex = data["x"].values, sharey = data["y"].values
for nn, ax in enumerate(axs.flat):
    column_name = stocks.dtype.names[1+nn]
    y = data["y"].values
    line, = ax.plot(stocks['Date'], y / np.nanmax(y), lw=2.5)
    ax.set_title(column_name, fontsize='small', loc='left')
fig.supxlabel('Year')
fig.supylabel('Stock price relative to max')

plt.show()

# %%
# .. tags::
#
#    component: figure
#    component: title
#    plot-type: line
#    level: beginner

import os