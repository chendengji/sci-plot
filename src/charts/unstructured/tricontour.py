"""Triangular contour plot - reference: plot_types_python/unstructured/tricontour.py"""


def plot(fig, ax, df, **kwargs):
    """Contour lines on irregular triangular grid."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    cntr = ax.tricontour(df[x_col], df[y_col], df[z_col],
                         levels=10, colors='black')
    ax.clabel(cntr, inline=True)
    ax.set_title(kwargs.get('title', 'Triangular Contour'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax