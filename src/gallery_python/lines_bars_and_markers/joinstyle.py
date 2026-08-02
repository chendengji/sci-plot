"""
=========
JoinStyle
=========

The `matplotlib._enums.JoinStyle` controls how Matplotlib draws the corners
where two different line segments meet. For more details, see the
`~matplotlib._enums.JoinStyle` docs.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

from matplotlib._enums import JoinStyle

JoinStyle.demo()
plt.show()

# %%
# .. tags:: purpose: reference, styling: linestyle

import os