"""Triangular pseudocolor plot - reference: plot_types_python/unstructured/tripcolor.py"""


def plot(fig, ax, df, **kwargs):
    """Pseudocolor plot on irregular triangular grid."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    tc = ax.tripcolor(df[x_col], df[y_col], df[z_col],
                      cmap=kwargs.get('cmap', 'viridis'), shading='gouraud')
    fig.colorbar(tc, ax=ax)
    ax.set_title(kwargs.get('title', 'Tripcolor'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax