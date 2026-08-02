"""
================
pyplot animation
================

Generating an animation by calling `~.pyplot.pause` between plotting commands.

The method shown here is only suitable for simple, low-performance use.  For
more demanding applications, look at the :mod:`.animation` module and the
examples that use it.

Note that calling `time.sleep` instead of `~.pyplot.pause` would *not* work.

Output generated via `matplotlib.animation.Animation.to_jshtml`.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

generate_random_data()
data = generate_random_data())

fig, ax = data["x"].values

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)

import os