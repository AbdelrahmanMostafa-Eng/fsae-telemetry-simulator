# test_comparison_plots.py

import numpy as np
import matplotlib
matplotlib.use("Agg")

from comparison_plots import ComparisonPlotter


def test_compare_laps_runs():
    pos = np.linspace(0, 100, 100)
    laps = {
        "Lap 1": np.linspace(10, 20, 100),
        "Lap 2": np.linspace(12, 22, 100),
    }

    plotter = ComparisonPlotter()
    plotter.compare_laps(pos, laps)


def test_compare_aero_runs():
    v = np.linspace(20, 100, 50)
    aero = {
        "Setup A": v**2,
        "Setup B": v**2 * 1.2,
    }

    plotter = ComparisonPlotter()
    plotter.compare_aero(v, aero)


def test_compare_telemetry_runs():
    t = np.linspace(0, 10, 200)
    signals = {
        "A": np.sin(t),
        "B": np.sin(t + 0.5),
    }

    plotter = ComparisonPlotter()
    plotter.compare_telemetry(t, signals)
