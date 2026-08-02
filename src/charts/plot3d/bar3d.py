"""3D bar plot - reference: plot_types_python/3D/bar3d_simple.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """3D bar chart."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    x_pos = np.arange(len(df))
    y_pos = np.zeros(len(df))

    ax.bar3d(x_pos, y_pos, np.zeros(len(df)), 0.5, 0.5, df[z_col].values,
             shade=True, alpha=0.8)
    ax.set_title(kwargs.get('title', '3D Bar Plot'))
    ax.set_zlabel(z_col)

    return ax