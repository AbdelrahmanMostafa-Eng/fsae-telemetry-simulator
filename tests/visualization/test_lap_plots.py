# test_lap_plots.py

import numpy as np
import matplotlib
matplotlib.use("Agg")

from lap_plots import LapPlotter


def test_speed_profile_plot_runs():
    pos = np.linspace(0, 100, 100)
    speeds = np.linspace(10, 20, 100)

    plotter = LapPlotter()
    plotter.plot_speed_profile(pos, speeds)


def test_acceleration_profile_plot_runs():
    pos = np.linspace(0, 100, 100)
    speeds = np.linspace(10, 20, 100)

    plotter = LapPlotter()
    plotter.plot_acceleration_profile(pos, speeds, dt=0.1)
