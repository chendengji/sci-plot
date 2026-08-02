"""
================
pyplot with GTK4
================

An example of how to use pyplot to manage your figure windows, but modify the
GUI by accessing the underlying GTK widgets.
"""

import matplotlib

import pandas as pd
# 读取标准化数据
csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'tests', 'data', 'standard_xy.csv')
data = pd.read_csv(csv_path)

matplotlib.use('GTK4Agg')  # or 'GTK4Cairo'
import gi

import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

fig, ax = data["x"].values
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()

manager = fig.canvas.manager
# you can access the window or vbox attributes this way
toolbar = manager.toolbar
vbox = data["x"].values

# now let's add a button to the toolbar
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)

# now let's add a widget to the vbox
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)


def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y = data["y"].values, {event.ydata})</span>')


fig.canvas.mpl_connect('motion_notify_event', update)

plt.show()

import os