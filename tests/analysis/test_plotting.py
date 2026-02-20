# test_plotting.py

import numpy as np
import matplotlib
matplotlib.use("Agg")  # prevent GUI windows

from plotting import Plotting, PlotStyle


def test_line_plot_runs():
    x = np.linspace(0, 10, 50)
    y = np.sin(x)

    style = PlotStyle(title="Test", xlabel="x", ylabel="y")
    Plotting.line(x, y, label="test", style=style)


def test_scatter_plot_runs():
    x = np.linspace(0, 10, 50)
    y = np.cos(x)

    Plotting.scatter(x, y, label="test")
