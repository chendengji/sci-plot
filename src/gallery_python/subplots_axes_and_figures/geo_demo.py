"""
======================
Geographic Projections
======================

This shows 4 possible geographic projections.  Cartopy_ supports more
projections.

.. _Cartopy: https://cartopy.readthedocs.io
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

# %%

plt.figure()
plt.subplot(projection="aitoff")
plt.title("Aitoff")
plt.grid(True)

# %%

plt.figure()
plt.subplot(projection="hammer")
plt.title("Hammer")
plt.grid(True)

# %%

plt.figure()
plt.subplot(projection="lambert")
plt.title("Lambert")
plt.grid(True)

# %%

plt.figure()
plt.subplot(projection="mollweide")
plt.title("Mollweide")
plt.grid(True)

plt.show()

# %%
# .. tags::
#
#    plot-type: specialty
#    component: projection
#    domain: cartography

import os