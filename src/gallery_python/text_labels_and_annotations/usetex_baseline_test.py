"""
====================
Usetex text baseline
====================

Comparison of text baselines computed for mathtext and usetex.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
axs = plt.figure(figsize=(2 * 3, 6.5)).subplots(1, 2)
for ax, usetex in zip(axs, [False, True]):
    ax.axvline(0, color="r")
    test_strings = ["lg", r"$\frac{1}{2}\pi$", r"$p^{3^A}$", r"$p_{3_2}$"]
    for i, s in enumerate(test_strings):
        ax.axhline(i, color="r")
        ax.text(0., 3 - i, s,
                usetex = data["x"].values,
                verticalalignment="baseline",
                size=50,
                bbox = data["x"].values, ec="k", fc="none"))
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[],
           title=f"usetex = data["x"].values
plt.show()

import os