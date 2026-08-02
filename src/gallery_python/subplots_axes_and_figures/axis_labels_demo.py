"""
===================
Axis label position
===================

Choose axis label position when calling `~.Axes.set_xlabel` and
`~.Axes.set_ylabel` as well as for colorbar.

"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)

fig, ax = data["x"].values

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
ax.set_ylabel('YLabel', loc='top')
ax.set_xlabel('XLabel', loc='left')
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')

plt.show()

# %%
# .. tags::
#
#    component: axis
#    styling: position
#    level: beginner
