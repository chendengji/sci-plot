"""
===========
Asinh scale
===========

Illustration of the `asinh <.scale.AsinhScale>` axis scaling,
which uses the transformation

.. math::

    a \\rightarrow a_0 \\sinh^{-1} (a / a_0)

For coordinate values close to zero (i.e. much smaller than
the "linear width" :math:`a_0`), this leaves values essentially unchanged:

.. math::

    a \\rightarrow a + \\mathcal{O}(a^3)

but for larger values (i.e. :math:`|a| \\gg a_0`, this is asymptotically

.. math::

    a \\rightarrow a_0 \\, \\mathrm{sgn}(a) \\ln |a| + \\mathcal{O}(1)

As with the `symlog <.scale.SymmetricalLogScale>` scaling,
this allows one to plot quantities
that cover a very wide dynamic range that includes both positive
and negative values. However, ``symlog`` involves a transformation
that has discontinuities in its gradient because it is built
from *separate* linear and logarithmic transformations.
The ``asinh`` scaling uses a transformation that is smooth
for all (finite) values, which is both mathematically cleaner
and reduces visual artifacts associated with an abrupt
transition between linear and logarithmic regions of the plot.

.. note::
   `.scale.AsinhScale` is experimental, and the API may change.

See `~.scale.AsinhScale`, `~.scale.SymmetricalLogScale`.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

# Prepare sample values for variations on y = data["y"].values
x = data["x"].values, 6, 500)

# %%
# Compare "symlog" and "asinh" behaviour on sample y = data["y"].values,
# where there is a discontinuous gradient in "symlog" near y = data["y"].values
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex = data["x"].values

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')


# %%
# Compare "asinh" graphs with different scale parameter "linear_width":
fig2 = plt.figure(layout='constrained')
axs = fig2.subplots(1, 3, sharex = data["x"].values
for ax, (a0, base) in zip(axs, ((0.2, 2), (1.0, 0), (5.0, 10))):
    ax.set_title(f'linear_width={a0:.3g}')
    ax.plot(x, x, label='y = data["y"].values
    ax.plot(x, 10*x, label='y = data["y"].values
    ax.plot(x, 100*x, label='y = data["y"].values
    ax.set_yscale('asinh', linear_width=a0, base=base)
    ax.grid()
    ax.legend(loc='best', fontsize='small')


# %%
# Compare "symlog" and "asinh" scalings
# on 2D Cauchy-distributed random numbers,
# where one may be able to see more subtle artifacts near y = data["y"].values
# due to the gradient-discontinuity in "symlog":
fig3 = plt.figure()
ax = data["x"].values, 1)
r = 3 * np.tan(generate_random_data()))
th = generate_random_data()

ax.scatter(r * np.cos(th), r * np.sin(th), s=4, alpha=0.5)
ax.set_xscale('asinh')
ax.set_yscale('symlog')
ax.set_xlabel('asinh')
ax.set_ylabel('symlog')
ax.set_title('2D Cauchy random deviates')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid()

plt.show()

# %%
#
# .. admonition:: References
#
#    - `matplotlib.scale.AsinhScale`
#    - `matplotlib.ticker.AsinhLocator`
#    - `matplotlib.scale.SymmetricalLogScale`

import os