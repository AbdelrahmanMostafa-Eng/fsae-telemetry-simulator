# test_telemetry_plots.py

import numpy as np
import matplotlib
matplotlib.use("Agg")

from telemetry_plots import TelemetryPlotter


def test_raw_vs_smooth_plot_runs():
    t = np.linspace(0, 10, 200)
    raw = np.sin(t)
    smooth = np.sin(t)

    plotter = TelemetryPlotter()
    plotter.plot_raw_vs_smooth(t, raw, smooth)


def test_acceleration_plot_runs():
    t = np.linspace(0, 10, 200)
    accel = np.cos(t)

    plotter = TelemetryPlotter()
    plotter.plot_acceleration(t, accel)


def test_overlay_plot_runs():
    t = np.linspace(0, 10, 200)
    signals = {"A": np.sin(t), "B": np.cos(t)}

    plotter = TelemetryPlotter()
    plotter.plot_overlay(t, signals)
