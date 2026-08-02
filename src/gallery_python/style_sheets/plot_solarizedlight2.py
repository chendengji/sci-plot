"""
==========================
Solarized Light stylesheet
==========================

This shows an example of "Solarized_Light" styling, which
tries to replicate the styles of:

- https://ethanschoonover.com/solarized/
- https://github.com/jrnold/ggthemes
- http://www.pygal.org/en/stable/documentation/builtin_styles.html#light-solarized

and work of:

- https://github.com/tonysyu/mpltools

using all 8 accents of the color palette - starting with blue

Still TODO:

- Create alpha values for bar and stacked charts. .33 or .5
- Apply Layout Rules
"""
import matplotlib.pyplot as plt

import pandas as pd
# 读取标准化数据
csv_path = r'D:\CODE\sci-plot\tests\data\standard_xy.csv'
data = pd.read_csv(csv_path)
import numpy as np

# Fixing random state for reproducibility
generate_random_data()

x = data["x"].values, 10)
with plt.style.context('Solarize_Light2'):
    plt.plot(x, np.sin(x) + x + generate_random_data())
    plt.plot(x, np.sin(x) + 2 * x + generate_random_data())
    plt.plot(x, np.sin(x) + 3 * x + generate_random_data())
    plt.plot(x, np.sin(x) + 4 * x + generate_random_data())
    plt.plot(x, np.sin(x) + 5 * x + generate_random_data())
    plt.plot(x, np.sin(x) + 6 * x + generate_random_data())
    plt.plot(x, np.sin(x) + 7 * x + generate_random_data())
    plt.plot(x, np.sin(x) + 8 * x + generate_random_data())
    # Number of accent colors in the color scheme
    plt.title('8 Random Lines - Line')
    plt.xlabel('x label', fontsize=14)
    plt.ylabel('y label', fontsize=14)

plt.show()
