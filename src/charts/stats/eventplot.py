"""Event plot - reference: plot_types_python/stats/eventplot.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Event plot showing positions of events."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())
    data = [df[df[x_col] == g][y_col].values for g in groups]

    # eventplot 不会自动使用颜色循环，需要手动设置
    colors = [ax._get_lines.get_next_color() for _ in range(len(groups))]
    ax.eventplot(data, labels=groups, colors=colors)
    ax.set_title(kwargs.get('title', 'Event Plot'))
    ax.set_ylabel('Group')
    ax.set_xlabel('Position')

    return ax