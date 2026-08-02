"""
===================
Usetex font effects
===================

This script demonstrates that font effects specified in your pdftex.map
are now supported in usetex mode.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)


def setfont(font):
    return rf'\font\a {font} at 14pt\a '


fig = plt.figure()
for y, font, text in zip(
    range(5),
    ['ptmr8r', 'ptmri8r', 'ptmro8r', 'ptmr8rn', 'ptmrr8re'],
    [f'Nimbus Roman No9 L {x}'
     for x in ['', 'Italics (real italics for comparison)',
               '(slanted)', '(condensed)', '(extended)']],
):
    fig.text(.1, 1 - (y + 1) / 6, setfont(font) + text, usetex = data["x"].values

fig.suptitle('Usetex font effects')
# Would also work if saving to pdf.
plt.show()

import os