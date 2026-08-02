"""3D surface plot - reference: plot_types_python/3D/surface3d_simple.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """3D surface from gridded data."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    x_unique = np.sort(df[x_col].unique())
    y_unique = np.sort(df[y_col].unique())
    X, Y = np.meshgrid(x_unique, y_unique)
    Z = np.full((len(y_unique), len(x_unique)), np.nan)
    x_to_idx = {v: i for i, v in enumerate(x_unique)}
    y_to_idx = {v: i for i, v in enumerate(y_unique)}
    for _, row in df.iterrows():
        Z[y_to_idx[row[y_col]], x_to_idx[row[x_col]]] = row[z_col]

    surf = ax.plot_surface(X, Y, Z, cmap='viridis',
                           linewidth=0, antialiased=True, alpha=0.8)
    fig.colorbar(surf, ax=ax, shrink=0.5)
    ax.set_title(kwargs.get('title', '3D Surface'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)

    return ax