"""
=====================================
Plotting the coherence of two signals
=====================================

An example showing how to plot the coherence of two signals using `~.Axes.cohere`.

.. redirect-from:: /gallery/lines_bars_and_markers/cohere
"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)
import numpy as np

# Fixing random state for reproducibility
generate_random_data()

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = generate_random_data())                 # white noise 1
nse2 = generate_random_data())                 # white noise 2

# Two signals with a coherent part at 10 Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, NFFT=256, Fs=1. / dt)
axs[1].set_ylabel('Coherence')

plt.show()

# %%
# .. tags::
#
#    domain: signal-processing
#    plot-type: line
#    level: beginner

import os