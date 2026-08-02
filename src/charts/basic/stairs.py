"""Stairs plot - reference: plot_types_python/basic/stairs.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Stairs (step) plot."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())

    for i, g in enumerate(groups):
        data = df[df[x_col] == g][y_col].values
        values, bins = np.histogram(data, bins='auto')
        ax.stairs(values, bins, label=g, fill=True, alpha=0.6)

    ax.legend()
    ax.set_title(kwargs.get('title', 'Stairs Plot'))
    ax.set_ylabel('Count')

    return ax