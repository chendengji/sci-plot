"""Stackplot - reference: plot_types_python/basic/stackplot.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Stacked area plot."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())
    pivot = df.groupby(x_col)[y_col].sum()
    x_pos = np.arange(len(groups))

    ax.stackplot(x_pos, pivot.values, labels=pivot.index.tolist(),
                 alpha=0.7, edgecolor='black', linewidth=0.5)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(groups)
    ax.legend(loc='upper left')
    ax.set_title(kwargs.get('title', 'Stackplot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax