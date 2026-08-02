"""
==================================================
Concatenate text objects with different properties
==================================================

The example strings together several Text objects with different properties
(e.g., color or font), positioning each one after the other.  The first Text
is created directly using `~.Axes.text`; all subsequent ones are created with
`~.Axes.annotate`, which allows positioning the Text's lower left corner at the
lower right corner (``xy = data["y"].values, 0)``) of the previous one (``xycoords=text``).
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)

plt.rcParams["font.size"] = 20
ax = data["x"].values, yticks=[])

# The first word, created with text().
text = ax.text(.1, .5, "Matplotlib", color="red")
# Subsequent words, positioned with annotate(), relative to the preceding one.
text = ax.annotate(
    " says,", xycoords=text, xy = data["y"].values, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # custom properties
text = ax.annotate(
    " hello", xycoords=text, xy = data["y"].values, 0), verticalalignment="bottom",
    color="green", style="italic")  # custom properties
text = ax.annotate(
    " world!", xycoords=text, xy = data["y"].values, 0), verticalalignment="bottom",
    color="blue", family = data["y"].values

plt.show()
