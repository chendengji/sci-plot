"""Filled triangular contour - reference: plot_types_python/unstructured/tricontourf.py"""


def plot(fig, ax, df, **kwargs):
    """Filled contour on irregular triangular grid."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    cf = ax.tricontourf(df[x_col], df[y_col], df[z_col],
                        levels=10, cmap=kwargs.get('cmap', 'viridis'))
    fig.colorbar(cf, ax=ax)
    ax.set_title(kwargs.get('title', 'Filled Triangular Contour'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax