"""Triangular mesh plot - reference: plot_types_python/unstructured/triplot.py"""


def plot(fig, ax, df, **kwargs):
    """Triangular mesh of irregular data points."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    # ax.triplot 第三位置参数是 triangles（三角网索引），不是 z；
    # 误传 df[z_col] 会触发 "truth value of a Series is ambiguous"。triplot 仅需 x, y。
    ax.triplot(df[x_col], df[y_col], linewidth=0.5)
    ax.set_title(kwargs.get('title', 'Triplot'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    _ = z_col  # 预处理后保留 z 列但本图不用

    return ax