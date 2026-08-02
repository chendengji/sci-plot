"""
=========
CapStyle
=========

The `matplotlib._enums.CapStyle` controls how Matplotlib draws the two
endpoints (caps) of an unclosed line. For more details, see the
`~matplotlib._enums.CapStyle` docs.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)

from matplotlib._enums import CapStyle

CapStyle.demo()
plt.show()

# %%
# .. tags::
#
#    purpose: reference
