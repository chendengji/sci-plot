"""
==============
Keypress event
==============

Show how to connect to keypress events.

.. note::
    This example exercises the interactive capabilities of Matplotlib, and this
    will not appear in the static documentation. Please run this code on your
    machine to see the interactivity.

    You can copy and paste individual parts, or download the entire example
    using the link at the bottom of the page.
"""
import sys

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np


def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key = data["y"].values
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()


# Fixing random state for reproducibility
generate_random_data()

fig, ax = data["x"].values

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(generate_random_data(), generate_random_data(), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
