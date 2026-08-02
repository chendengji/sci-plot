"""Fill between plot - reference: plot_types_python/basic/fill_between.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Line plot with filled confidence band."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())
    x_pos = np.arange(len(groups))
    means = df.groupby(x_col)[y_col].mean()
    errs = df.groupby(x_col)[y_col].std()

    ax.plot(x_pos, means.values, 'o-', linewidth=1.5, markersize=6)
    ax.fill_between(x_pos, means.values - errs.values,
                    means.values + errs.values, alpha=0.3)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(groups)
    ax.set_title(kwargs.get('title', 'Fill Between Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax