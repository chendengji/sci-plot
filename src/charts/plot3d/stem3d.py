"""3D stem plot - reference: plot_types_python/3D/stem3d.py"""


def plot(fig, ax, df, **kwargs):
    """3D stem plot."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    ax.stem(df[x_col], df[y_col], df[z_col])
    ax.set_title(kwargs.get('title', '3D Stem Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)

    return ax