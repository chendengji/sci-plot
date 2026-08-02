"""Box plot - reference: plot_types_python/stats/boxplot_plot.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Box plot grouped by category."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())
    data = [df[df[x_col] == g][y_col].values for g in groups]

    bp = ax.boxplot(data, labels=groups, patch_artist=True,
                    boxprops=dict(linewidth=0.8),
                    whiskerprops=dict(linewidth=0.8),
                    capprops=dict(linewidth=0.8),
                    medianprops=dict(color='orange', linewidth=1.2))

    # 应用颜色循环，每组不同颜色
    colors = [ax._get_lines.get_next_color() for _ in range(len(groups))]
    for i, patch in enumerate(bp['boxes']):
        patch.set_facecolor(colors[i % len(colors)])
        patch.set_alpha(0.7)

    ax.set_title(kwargs.get('title', 'Box Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax