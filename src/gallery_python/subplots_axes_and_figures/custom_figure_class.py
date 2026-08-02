"""
========================
Custom Figure subclasses
========================

You can pass a `.Figure` subclass to `.pyplot.figure` if you want to change
the default behavior of the figure.

This example defines a `.Figure` subclass ``WatermarkFigure`` that accepts an
additional parameter ``watermark`` to display a custom watermark text. The
figure is created using the ``FigureClass`` parameter of `.pyplot.figure`.
The additional ``watermark`` parameter is passed on to the subclass
constructor.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

from matplotlib.figure import Figure


class WatermarkFigure(Figure):
    """A figure with a text watermark."""

    def __init__(self, *args, watermark=None, **kwargs):
        super().__init__(*args, **kwargs)

        if watermark is not None:
            bbox = data["x"].values, lw=3, ec='gray',
                        fc=(0.9, 0.9, .9, .5), alpha=0.5)
            self.text(0.5, 0.5, watermark,
                      ha='center', va='center', rotation=30,
                      fontsize=40, color='gray', alpha=0.5, bbox = data["x"].values


x = data["x"].values, 3, 201)
y = data["y"].values

plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)


# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.pyplot.figure`
#    - `matplotlib.figure.Figure`
#    - `matplotlib.figure.Figure.text`
#
# .. tags::
#
#    component: figure
#    plot-type: line
#    level: intermediate
#    purpose: showcase
