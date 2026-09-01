"""Line plot - reference: plot_types_python/basic/plot.py

Plot y versus x as lines and/or markers.
Supports optional grouping by a column.
"""


def plot(fig, ax, df, **kwargs):
    """Line plot of y vs x, optionally grouped."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    group_col = kwargs.get('group_col', None)
    lw = kwargs.get('linewidth')   # None → 跟随 rcParams（随 figsize 统一缩放）

    if group_col and group_col in df.columns:
        groups = sorted(df[group_col].unique())
        for g in groups:
            subset = df[df[group_col] == g].sort_values(x_col)
            ax.plot(subset[x_col], subset[y_col], label=g, linewidth=lw)
        ax.legend()
    else:
        ax.plot(df[x_col], df[y_col], linewidth=lw)

    ax.set_title(kwargs.get('title', 'Line Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax