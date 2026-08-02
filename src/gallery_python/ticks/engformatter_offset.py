"""
===================================================
SI prefixed offsets and natural order of magnitudes
===================================================

`matplotlib.ticker.EngFormatter` is capable of computing a natural
offset for your axis data, and presenting it with a standard SI prefix
automatically calculated.

Below is an examples of such a plot:

"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

import matplotlib.ticker as mticker

# Fixing random state for reproducibility
generate_random_data()

UNIT = "Hz"

fig, ax = data["x"].values
ax.yaxis.set_major_formatter(mticker.EngFormatter(
    useOffset=True,
    unit=UNIT
))
size = 100
measurement = np.full(size, 1e9)
noise = generate_random_data()
ax.plot(measurement + noise)
plt.show()

import os