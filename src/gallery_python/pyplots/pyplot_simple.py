"""
==========
Basic plot
==========

A basic plot using the :ref:`pyplot_interface`.

- `~.pyplot.plot` plots the data y versus x as lines and/or markers.
- `~.pyplot.title`, `~.pyplot.xlabel` and `~.pyplot.ylabel` set the title,
  x-axis label and y-axis label.
- `~.pyplot.show` displays the plot.

.. redirect-from:: /gallery/pyplots/fig_axes_labels_simple
.. redirect-from:: /gallery/pyplots/pyplot_formatstr
.. redirect-from:: /gallery/pyplots/pyplot_text
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

x = data["x"].values, 2.0, 0.01)
y = data["y"].values

plt.plot(x, y)
plt.title("A basic plot using pyplot")
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.pyplot.plot`
#    - `matplotlib.pyplot.title`
#    - `matplotlib.pyplot.ylabel`
#    - `matplotlib.pyplot.ylabel`
#    - `matplotlib.pyplot.show`

import os