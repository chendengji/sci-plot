"""Triangular mesh plot - reference: plot_types_python/unstructured/triplot.py"""


def plot(fig, ax, df, **kwargs):
    """Triangular mesh of irregular data points."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    ax.triplot(df[x_col], df[y_col], df[z_col], linewidth=0.5)
    ax.set_title(kwargs.get('title', 'Triplot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax