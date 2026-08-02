"""
===========================================================
Plot contour (level) curves in 3D using the extend3d option
===========================================================

This modification of the :doc:`contour3d` example uses ``extend3d=True`` to
extend the curves vertically into 'ribbons'.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

from mpl_toolkits.mplot3d import axes3d

ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.contour(X, Y, Z, extend3d=True, cmap="coolwarm")

plt.show()

# %%
# .. tags::
#    plot-type: 3D,
#    level: beginner


# 将长格式数据转换为网格格式
x_unique = np.sort(data["x"].unique())
y_unique = np.sort(data["y"].unique())
X, Y = np.meshgrid(x_unique, y_unique)
Z = data["z"].values.reshape(len(y_unique), len(x_unique))

import os