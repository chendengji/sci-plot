"""Violin plot - reference: plot_types_python/stats/violin.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Violin plot grouped by category."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())
    data = [df[df[x_col] == g][y_col].values for g in groups]

    parts = ax.violinplot(data, showmeans=True, showmedians=True)

    # 应用颜色循环，每组不同颜色
    colors = [ax._get_lines.get_next_color() for _ in range(len(groups))]
    for i, pc in enumerate(parts['bodies']):
        pc.set_facecolor(colors[i % len(colors)])
        pc.set_alpha(0.7)
        pc.set_edgecolor('black')
    for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans'):
        if partname in parts:
            parts[partname].set_edgecolor('black')
            parts[partname].set_linewidth(1)

    ax.set_xticks(range(1, len(groups) + 1))
    ax.set_xticklabels(groups)
    ax.set_title(kwargs.get('title', 'Violin Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax