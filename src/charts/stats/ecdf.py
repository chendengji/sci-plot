"""ECDF plot - reference: plot_types_python/stats/ecdf.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Empirical Cumulative Distribution Function."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())

    for i, g in enumerate(groups):
        data = df[df[x_col] == g][y_col].values
        ax.ecdf(data, label=g)

    ax.legend()
    ax.set_title(kwargs.get('title', 'ECDF Plot'))
    ax.set_xlabel(y_col)
    ax.set_ylabel('Empirical CDF')

    return ax