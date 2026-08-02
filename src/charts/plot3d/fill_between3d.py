"""3D fill between plot - reference: plot_types_python/3D/fill_between3d_simple.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """3D fill between curves."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    groups = sorted(df[x_col].unique())
    for g in groups:
        subset = df[df[x_col] == g].sort_values(y_col)
        ax.fill_between(subset[y_col], subset[z_col], alpha=0.5, label=g)

    ax.legend()
    ax.set_title(kwargs.get('title', '3D Fill Between'))
    ax.set_xlabel(y_col)
    ax.set_ylabel(z_col)

    return ax