"""3D voxels plot - reference: plot_types_python/3D/voxels_simple.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """3D voxels visualization."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')
    v_col = kwargs.get('v_col', z_col)

    x_unique = sorted(df[x_col].unique())
    y_unique = sorted(df[y_col].unique())
    z_unique = sorted(df[z_col].unique())

    voxels = np.zeros((len(x_unique), len(y_unique), len(z_unique)), dtype=bool)
    for _, row in df.iterrows():
        ix = x_unique.index(row[x_col])
        iy = y_unique.index(row[y_col])
        iz = z_unique.index(row[z_col])
        if row[v_col] > 0:
            voxels[ix, iy, iz] = True

    ax.voxels(voxels, edgecolor='k', linewidth=0.1, alpha=0.8)
    ax.set_title(kwargs.get('title', 'Voxels'))

    return ax