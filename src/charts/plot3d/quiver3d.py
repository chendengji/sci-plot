"""3D quiver plot - reference: plot_types_python/3D/quiver3d_simple.py"""


def plot(fig, ax, df, **kwargs):
    """3D vector field (quiver) plot."""
    x_col = kwargs.get('x_col')
    y_col = kwargs.get('y_col')
    z_col = kwargs.get('z_col')
    u_col = kwargs.get('u_col')
    v_col = kwargs.get('v_col')
    w_col = kwargs.get('w_col')

    ax.quiver(df[x_col], df[y_col], df[z_col],
              df[u_col], df[v_col], df[w_col], length=0.5, alpha=0.7)
    ax.set_title(kwargs.get('title', '3D Quiver'))
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)

    return ax