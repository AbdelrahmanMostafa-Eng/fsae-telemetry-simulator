# lap_plots.py

"""
Visualization utilities for lap simulation results.
Provides:
- Speed profile plotting
- Acceleration profile plotting
- Optional integration with global style settings

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class LapPlotter:
    title: str = "Lap Visualization"
    xlabel: str = "Track Position (units)"
    ylabel_speed: str = "Speed (km/h)"
    ylabel_accel: str = "Acceleration (m/s²)"

    def plot_speed_profile(self, positions: np.ndarray, speeds: np.ndarray):
        """Plot speed profile along the lap."""
        plt.figure(figsize=(10, 4))
        plt.plot(positions, speeds * 3.6, label="Speed")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel_speed)
        plt.title(f"{self.title} — Speed Profile")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_acceleration_profile(self, positions: np.ndarray, speeds: np.ndarray, dt: float):
        """Plot acceleration computed from speed data."""
        accel = np.zeros_like(speeds)
        accel[1:-1] = (speeds[2:] - speeds[:-2]) / (2 * dt)
        accel[0] = accel[1]
        accel[-1] = accel[-2]

        plt.figure(figsize=(10, 4))
        plt.plot(positions, accel, label="Acceleration", color="orange")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel_accel)
        plt.title(f"{self.title} — Acceleration Profile")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


# Example usage

if __name__ == "__main__":
    pos = np.linspace(0, 300, 300)
    speeds = 30 + 10 * np.sin(pos / 40)

    plotter = LapPlotter(title="Demo Lap")
    plotter.plot_speed_profile(pos, speeds)
    plotter.plot_acceleration_profile(pos, speeds, dt=0.1)
