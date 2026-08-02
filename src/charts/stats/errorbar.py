"""Errorbar plot - reference: plot_types_python/stats/errorbar_plot.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Errorbar plot (mean ± std by group)."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())
    x_pos = np.arange(len(groups))
    means = [df[df[x_col] == g][y_col].mean() for g in groups]
    errs = [df[df[x_col] == g][y_col].std() for g in groups]

    ax.errorbar(x_pos, means, yerr=errs, fmt='-o',
                capsize=5, markersize=6, elinewidth=1.2)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(groups)
    ax.set_title(kwargs.get('title', 'Errorbar Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax