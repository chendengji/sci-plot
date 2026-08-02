"""Histogram - reference: plot_types_python/stats/hist_plot.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Histogram with grouped overlay."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())

    for i, g in enumerate(groups):
        data = df[df[x_col] == g][y_col].values
        ax.hist(data, bins=20, density=False, histtype='stepfilled',
                alpha=0.7, label=g, edgecolor='black', linewidth=0.5)

    ax.legend()
    ax.set_title(kwargs.get('title', 'Histogram'))
    ax.set_xlabel(y_col)
    ax.set_ylabel('Density')

    return ax