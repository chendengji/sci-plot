"""2D Histogram - reference: plot_types_python/stats/hist2d.py"""


def plot(fig, ax, df, **kwargs):
    """2D histogram (needs two numeric columns)."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')

    if x_col is None or y_col is None:
        cols = df.select_dtypes(include='number').columns[:2]
        x_col, y_col = cols[0], cols[1]

    h = ax.hist2d(df[x_col], df[y_col], bins=20, cmap='viridis')
    fig.colorbar(h[3], ax=ax)
    ax.set_title(kwargs.get('title', '2D Histogram'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax