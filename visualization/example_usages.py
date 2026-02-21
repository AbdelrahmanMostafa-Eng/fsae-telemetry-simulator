# example_usages.py

"""
Integration demo for visualization modules:
- style.py
- lap_plots.py
- aero_plots.py
- telemetry_plots.py
- comparison_plots.py
"""

import numpy as np

from style import apply_style, PlotStyleConfig
from lap_plots import LapPlotter
from aero_plots import AeroPlotter
from telemetry_plots import TelemetryPlotter
from comparison_plots import ComparisonPlotter


# ---------------------------------------------------------
# Apply global style
# ---------------------------------------------------------

apply_style(PlotStyleConfig(font_size=12))


# ---------------------------------------------------------
# Lap Visualization
# ---------------------------------------------------------

positions = np.linspace(0, 300, 300)
speeds = 30 + 10 * np.sin(positions / 40)

lap_plotter = LapPlotter(title="Visualization Demo Lap")
lap_plotter.plot_speed_profile(positions, speeds)
lap_plotter.plot_acceleration_profile(positions, speeds, dt=0.1)


# ---------------------------------------------------------
# Aerodynamic Visualization
# ---------------------------------------------------------

velocities = np.linspace(20, 100, 60)
drag = 0.5 * 1.225 * 1.0 * 1.5 * velocities**2
downforce = 0.5 * 1.225 * 3.0 * 1.5 * velocities**2

aero_plotter = AeroPlotter(title="Visualization Demo Aero")
aero_plotter.plot_drag(velocities, drag)
aero_plotter.plot_downforce(velocities, downforce)
aero_plotter.plot_aero_map(velocities, drag, downforce)


# ---------------------------------------------------------
# Telemetry Visualization
# ---------------------------------------------------------

t = np.linspace(0, 10, 500)
raw_signal = 20 + 5 * np.sin(2 * np.pi * 0.5 * t) + np.random.normal(0, 0.8, len(t))
smooth_signal = 20 + 5 * np.sin(2 * np.pi * 0.5 * t)
accel = np.gradient(smooth_signal, t[1] - t[0])

telemetry_plotter = TelemetryPlotter(title="Visualization Demo Telemetry")
telemetry_plotter.plot_raw_vs_smooth(t, raw_signal, smooth_signal)
telemetry_plotter.plot_acceleration(t, accel)
telemetry_plotter.plot_overlay(t, {"Raw": raw_signal, "Smooth": smooth_signal, "Accel": accel})


# ---------------------------------------------------------
# Comparison Visualization
# ---------------------------------------------------------

comparison_plotter = ComparisonPlotter(
    title="Visualization Demo Comparison",
    xlabel="Time (s)",
    ylabel="Signal"
)

comparison_plotter.compare_telemetry(
    t,
    {
        "Signal A": np.sin(t),
        "Signal B": np.sin(t + 0.5),
        "Signal C": np.sin(t + 1.0),
    }
)
