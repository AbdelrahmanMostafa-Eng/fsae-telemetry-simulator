# test_aero_plots.py

import numpy as np
import matplotlib
matplotlib.use("Agg")

from aero_plots import AeroPlotter


def test_drag_plot_runs():
    v = np.linspace(20, 100, 50)
    drag = v**2

    plotter = AeroPlotter()
    plotter.plot_drag(v, drag)


def test_downforce_plot_runs():
    v = np.linspace(20, 100, 50)
    df = v**2

    plotter = AeroPlotter()
    plotter.plot_downforce(v, df)


def test_aero_map_plot_runs():
    v = np.linspace(20, 100, 50)
    drag = v**2
    df = v**2 * 2

    plotter = AeroPlotter()
    plotter.plot_aero_map(v, drag, df)
