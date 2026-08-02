"""
================
Simple Axisline3
================

"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

from mpl_toolkits.axisartist.axislines import Axes

fig = plt.figure(figsize=(3, 3))

ax = data["x"].values

ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)

plt.show()

import os