"""Hexbin plot - reference: plot_types_python/stats/hexbin.py"""


def plot(fig, ax, df, **kwargs):
    """Hexbin 2D density plot (needs two numeric columns)."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')

    if x_col is None or y_col is None:
        cols = df.select_dtypes(include='number').columns[:2]
        x_col, y_col = cols[0], cols[1]

    hb = ax.hexbin(df[x_col], df[y_col], gridsize=20, cmap='viridis')
    fig.colorbar(hb, ax=ax)
    ax.set_title(kwargs.get('title', 'Hexbin Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax