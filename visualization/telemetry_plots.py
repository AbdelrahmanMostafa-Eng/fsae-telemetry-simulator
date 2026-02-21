# telemetry_plots.py

"""
Visualization utilities for telemetry signal analysis.
Provides:
- Raw vs smoothed signal plotting
- Acceleration plotting
- Combined telemetry overlays

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class TelemetryPlotter:
    title: str = "Telemetry Visualization"
    xlabel: str = "Time (s)"
    ylabel_signal: str = "Signal"
    ylabel_accel: str = "Acceleration (m/s²)"

    def plot_raw_vs_smooth(self, t: np.ndarray, raw: np.ndarray, smooth: np.ndarray):
        """Plot raw and smoothed telemetry signals."""
        plt.figure(figsize=(10, 4))
        plt.plot(t, raw, alpha=0.4, label="Raw")
        plt.plot(t, smooth, label="Smoothed", linewidth=2)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel_signal)
        plt.title(f"{self.title} — Raw vs Smoothed")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_acceleration(self, t: np.ndarray, accel: np.ndarray):
        """Plot acceleration signal."""
        plt.figure(figsize=(10, 4))
        plt.plot(t, accel, label="Acceleration", color="orange")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel_accel)
        plt.title(f"{self.title} — Acceleration")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_overlay(self, t: np.ndarray, signals: dict):
        """
        Plot multiple telemetry signals on the same axes.
        signals: dict {label: array}
        """
        plt.figure(figsize=(10, 4))
        for label, sig in signals.items():
            plt.plot(t, sig, label=label)

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel_signal)
        plt.title(f"{self.title} — Overlay")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


# Example usage

if __name__ == "__main__":
    t = np.linspace(0, 10, 500)
    raw = 20 + 5 * np.sin(2 * np.pi * 0.5 * t) + np.random.normal(0, 0.8, len(t))
    smooth = 20 + 5 * np.sin(2 * np.pi * 0.5 * t)
    accel = np.gradient(smooth, t[1] - t[0])

    plotter = TelemetryPlotter(title="Demo Telemetry")
    plotter.plot_raw_vs_smooth(t, raw, smooth)
    plotter.plot_acceleration(t, accel)
    plotter.plot_overlay(t, {"Raw": raw, "Smooth": smooth, "Accel": accel})
