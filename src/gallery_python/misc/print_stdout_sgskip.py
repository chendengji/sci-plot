"""
=====================
Print image to stdout
=====================

print png to standard out

usage: python print_stdout.py > somefile.png

"""

import sys

import matplotlib

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)

matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot([1, 2, 3])
plt.savefig(sys.stdout.buffer)
