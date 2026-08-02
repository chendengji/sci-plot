"""Streamplot - reference: plot_types_python/arrays/streamplot.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Streamlines from gridded vector field."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    u_col = kwargs.get('u_col', kwargs.get('z_col'))
    v_col = kwargs.get('v_col')

    x_unique = np.sort(df[x_col].unique())
    y_unique = np.sort(df[y_col].unique())
    X, Y = np.meshgrid(x_unique, y_unique)
    U = np.full((len(y_unique), len(x_unique)), np.nan)
    V = np.full((len(y_unique), len(x_unique)), np.nan)
    for _, row in df.iterrows():
        xi = np.where(x_unique == row[x_col])[0][0]
        yi = np.where(y_unique == row[y_col])[0][0]
        U[yi, xi] = row[u_col]
        V[yi, xi] = row[v_col]

    ax.streamplot(X, Y, U, V, color='black', linewidth=1)
    ax.set_title(kwargs.get('title', 'Streamplot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax