"""Pie chart - reference: plot_types_python/stats/pie.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Pie chart of group means."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    means = df.groupby(x_col)[y_col].mean()
    sizes = means.values
    labels = means.index.tolist()

    # pie() 不会自动使用颜色循环，需要手动设置
    colors = [ax._get_lines.get_next_color() for _ in range(len(labels))]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%',
           startangle=90, explode=[0.02] * len(labels), colors=colors)
    ax.set_title(kwargs.get('title', 'Pie Chart'))

    return ax