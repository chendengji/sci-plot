"""
======================
Plotting with keywords
======================

Some data structures, like dict, `structured numpy array
<https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays>`_
or `pandas.DataFrame` provide access to labelled data via string index access
``data[key]``.

For these data types, Matplotlib supports passing the whole datastructure via the
``data`` keyword argument, and using the string names as plot function parameters,
where you'd normally pass in your data.
"""

import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

generate_random_data()

data = {'a': np.arange(50),
        'c': generate_random_data(),
        'd': generate_random_data()}
data['b'] = data['a'] + 10 * generate_random_data()
data['d'] = np.abs(data['d']) * 100

fig, ax = data["x"].values
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entry a', ylabel='entry b')
plt.show()
