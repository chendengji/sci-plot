"""Bar chart - reference: plot_types_python/basic/bar.py"""

import numpy as np


def plot(fig, ax, df, **kwargs):
    """Grouped bar chart with error bars."""
    x_col = kwargs.get('x_col', 'group')
    y_col = kwargs.get('y_col', 'value')

    groups = sorted(df[x_col].unique())
    means = df.groupby(x_col)[y_col].mean()
    errs = df.groupby(x_col)[y_col].std()
    x_pos = np.arange(len(groups))

    bars = ax.bar(x_pos, means.values, yerr=errs.values, capsize=5,
                  width=0.5, ecolor='black', edgecolor='black', linewidth=0.8)

    # 应用颜色循环，每组不同颜色
    for i, bar in enumerate(bars):
        color = ax._get_lines.get_next_color()
        bar.set_facecolor(color)

    ax.set_xticks(x_pos)
    ax.set_xticklabels(groups)
    ax.set_title(kwargs.get('title', 'Bar Plot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    return ax