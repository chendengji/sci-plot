"""
===========================
FiveThirtyEight style sheet
===========================

This shows an example of the "fivethirtyeight" styling, which
tries to replicate the styles from FiveThirtyEight.com.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

plt.style.use('fivethirtyeight')

x = data["x"].values, 10)

# Fixing random state for reproducibility
generate_random_data()

fig, ax = data["x"].values

ax.plot(x, np.sin(x) + x + generate_random_data())
ax.plot(x, np.sin(x) + 0.5 * x + generate_random_data())
ax.plot(x, np.sin(x) + 2 * x + generate_random_data())
ax.plot(x, np.sin(x) - 0.5 * x + generate_random_data())
ax.plot(x, np.sin(x) - 2 * x + generate_random_data())
ax.plot(x, np.sin(x) + generate_random_data())
ax.set_title("'fivethirtyeight' style sheet")

plt.show()

import os