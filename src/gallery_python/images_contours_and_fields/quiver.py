#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=======================================
Advanced quiver and quiverkey functions
=======================================

Demonstrates some more advanced options for `~.axes.Axes.quiver` using
standardized test data.

**改造说明**: 原始脚本使用 np.meshgrid 和三角函数生成向量场，
已改造为使用标准化 CSV 数据文件 (standard_vector.csv)。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取标准化测试数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tests', 'data', 'standard_vector.csv')
data = pd.read_csv(csv_path)

# 准备向量场数据
x = data['x'].values
y = data['y'].values
u = data['u'].values
v = data['v'].values

# 重新网格化（如果原始数据不是网格格式）
if len(np.unique(x)) < 10:
    X = np.linspace(x.min(), x.max(), 15)
    Y = np.linspace(y.min(), y.max(), 15)
    X, Y = np.meshgrid(X, Y)
    # 使用插值
    from scipy.interpolate import griddata
    U = griddata((x, y), u, (X, Y), method='cubic')
    V = griddata((x, y), v, (X, Y), method='cubic')
else:
    # 假设原始数据已经是网格格式
    X = x.reshape(int(len(x)**0.5), int(len(x)**0.5))
    Y = y.reshape(int(len(y)**0.5), int(len(y)**0.5))
    U = u.reshape(int(len(u)**0.5), int(len(u)**0.5))
    V = v.reshape(int(len(v)**0.5), int(len(v)**0.5))

# %%

fig1, ax1 = plt.subplots()
ax1.set_title('Quiver Plot from Standardized Vector Data')
Q = ax1.quiver(X, Y, U, V, units='width', color='steelblue')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')

# %%

fig2, ax2 = plt.subplots()
ax2.set_title("pivot='middle'; units='inches'")
Q = ax2.quiver(X, Y, U, V, pivot='middle', units='inches', color='coral')
qk = ax2.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax2.scatter(X, Y, color='red', s=5)

# %%

fig3, ax3 = plt.subplots()
ax3.set_title("pivot='tip'; scales with x view")
M = np.hypot(U, V)
Q = ax3.quiver(X, Y, U, V, M, units='x', pivot='tip', width=0.022,
               scale=1 / 0.15, color='green')
qk = ax3.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax3.scatter(X, Y, color='gray', s=1)

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.quiver` / `matplotlib.pyplot.quiver`
#    - `matplotlib.axes.Axes.quiverkey` / `matplotlib.pyplot.quiverkey`

import os