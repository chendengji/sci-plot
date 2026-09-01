"""Filled contour plot - reference: plot_types_python/arrays/contourf.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Filled contour from gridded data."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    x_unique = sorted(df[x_col].unique())
    y_unique = sorted(df[y_col].unique())
    X, Y = np.meshgrid(x_unique, y_unique)
    Z = np.full((len(y_unique), len(x_unique)), np.nan)
    x_to_idx = {v: i for i, v in enumerate(x_unique)}
    y_to_idx = {v: i for i, v in enumerate(y_unique)}
    for _, row in df.iterrows():
        Z[y_to_idx[row[y_col]], x_to_idx[row[x_col]]] = row[z_col]

    cf = ax.contourf(X, Y, Z, levels=10, cmap=kwargs.get('cmap', 'viridis'))
    fig.colorbar(cf, ax=ax)
    ax.set_title(kwargs.get('title', 'Filled Contour Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax