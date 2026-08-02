"""
====================
List of named colors
====================

This plots a list of the named colors supported by Matplotlib.
For more information on colors in matplotlib see

* the :ref:`colors_def` tutorial;
* the `matplotlib.colors` API;
* the :doc:`/gallery/color/color_demo`.

----------------------------
Helper Function for Plotting
----------------------------
First we define a helper function for making a table of colors, then we use it
on some common color categories.
"""

import math

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)

import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle


def plot_colortable(colors, *, ncols=4, sort_colors=True):

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key = data["y"].values
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = data["x"].values, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = data["y"].values

        swatch_start_x = data["x"].values
        text_pos_x = data["x"].values

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy = data["y"].values, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig

# %%
# -----------
# Base colors
# -----------

plot_colortable(mcolors.BASE_COLORS, ncols=3, sort_colors=False)

# %%
# ---------------
# Tableau Palette
# ---------------

plot_colortable(mcolors.TABLEAU_COLORS, ncols=2, sort_colors=False)

# %%
# ----------
# CSS Colors
# ----------

# sphinx_gallery_thumbnail_number = 3
plot_colortable(mcolors.CSS4_COLORS)
plt.show()

# %%
# -----------
# XKCD Colors
# -----------
# Matplotlib supports colors from the
# `xkcd color survey <https://xkcd.com/color/rgb/>`_, e.g. ``"xkcd:sky blue"``. Since
# this contains almost 1000 colors, a figure of this would be very large and is thus
# omitted here. You can use the following code to generate the overview yourself ::
#
#     xkcd_fig = plot_colortable(mcolors.XKCD_COLORS)
#     xkcd_fig.savefig("XKCD_Colors.png")
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.colors`
#    - `matplotlib.colors.rgb_to_hsv`
#    - `matplotlib.colors.to_rgba`
#    - `matplotlib.figure.Figure.get_size_inches`
#    - `matplotlib.figure.Figure.subplots_adjust`
#    - `matplotlib.axes.Axes.text`
#    - `matplotlib.patches.Rectangle`
#
# .. tags::
#
#    styling: color
#    purpose: reference
