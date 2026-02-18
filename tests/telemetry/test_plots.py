#test_plots.py

"""
Unit tests for telemetry.plots.
"""

import matplotlib
matplotlib.use("Agg")  # Prevents GUI windows during tests

from telemetry.plots import TelemetryPlots
import numpy as np


def test_plot_lap_times():
    lap_times = np.array([60, 61, 62, 63])
    fig = TelemetryPlots.plot_lap_times(lap_times)
    assert fig is not None


def test_plot_speeds():
    speeds = np.array([120, 125, 130, 128])
    fig = TelemetryPlots.plot_speeds(speeds)
    assert fig is not None


def test_plot_fuel_usage():
    fuel = np.array([0, 1, 2, 3])
    fig = TelemetryPlots.plot_fuel_usage(fuel)
    assert fig is not None


def test_plot_tire_wear():
    wear = np.array([0, 5, 10, 15])
    fig = TelemetryPlots.plot_tire_wear(wear)
    assert fig is not None
