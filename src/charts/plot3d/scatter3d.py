"""3D scatter plot - reference: plot_types_python/3D/scatter3d_simple.py"""


def plot(fig, ax, df, **kwargs):
    """3D scatter plot."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')
    c_col = kwargs.get('c_col', None)

    sc = ax.scatter(df[x_col], df[y_col], df[z_col],
                    c=df[c_col] if c_col else None,
                    cmap='viridis', s=30, alpha=0.7)
    if c_col:
        fig.colorbar(sc, ax=ax, shrink=0.5)
    ax.set_title(kwargs.get('title', '3D Scatter'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)

    return ax