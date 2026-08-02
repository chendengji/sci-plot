"""Scatter plot - reference: plot_types_python/basic/scatter_plot.py

A scatter plot of y versus x with optional grouping.
"""


def plot(fig, ax, df, **kwargs):
    """Scatter plot of y vs x, optionally grouped."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    group_col = kwargs.get('group_col', None)

    if group_col and group_col in df.columns:
        groups = sorted(df[group_col].unique())
        for g in groups:
            subset = df[df[group_col] == g]
            ax.scatter(subset[x_col], subset[y_col], label=g, alpha=0.7, s=20)
        ax.legend()
    else:
        ax.scatter(df[x_col], df[y_col], alpha=0.7, s=20)

    ax.set_title(kwargs.get('title', 'Scatter Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax