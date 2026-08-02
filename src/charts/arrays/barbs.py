"""Barb plot - reference: plot_types_python/arrays/barbs.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Wind barb plot."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    u_col = kwargs.get('u_col', kwargs.get('z_col'))
    v_col = kwargs.get('v_col', u_col)

    ax.barbs(df[x_col], df[y_col], df[u_col], df[v_col], length=5, alpha=0.7)
    ax.set_title(kwargs.get('title', 'Barb Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax