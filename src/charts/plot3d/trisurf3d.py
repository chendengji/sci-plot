"""3D triangulated surface - reference: plot_types_python/3D/trisurf3d_simple.py"""


def plot(fig, ax, df, **kwargs):
    """3D triangulated surface from irregular data."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')

    surf = ax.plot_trisurf(df[x_col], df[y_col], df[z_col],
                           cmap=kwargs.get('cmap', 'viridis'), linewidth=0, alpha=0.8)
    fig.colorbar(surf, ax=ax, shrink=0.5)
    ax.set_title(kwargs.get('title', '3D Triangulated Surface'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)

    return ax