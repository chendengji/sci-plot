"""Stem plot - reference: plot_types_python/basic/stem.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Stem plot grouped by category."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())

    for i, g in enumerate(groups):
        data = df[df[x_col] == g][y_col].values
        markerline, stemlines, baseline = ax.stem(
            data, label=g, linefmt='-', markerfmt='o', basefmt=' ')
        stemlines.set_linewidth(1.5)
        markerline.set_markersize(5)

    ax.legend()
    ax.set_title(kwargs.get('title', 'Stem Plot'))
    ax.set_xlabel('Index')
    ax.set_ylabel(y_col)

    return ax