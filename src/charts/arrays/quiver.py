"""Quiver plot - reference: plot_types_python/arrays/quiver.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Vector field (quiver) plot."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    u_col = kwargs.get('u_col')
    v_col = kwargs.get('v_col')

    if u_col is None:
        u_col = kwargs.get('z_col', df.columns[2])
    if v_col is None:
        v_col = df.columns[3] if len(df.columns) > 3 else u_col

    ax.quiver(df[x_col], df[y_col], df[u_col], df[v_col], alpha=0.7)
    ax.set_title(kwargs.get('title', 'Quiver Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax