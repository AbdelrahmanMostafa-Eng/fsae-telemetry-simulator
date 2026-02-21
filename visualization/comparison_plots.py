# comparison_plots.py

"""
Visualization utilities for comparing multiple datasets.
Provides:
- Lap speed comparison
- Aerodynamic force comparison
- Telemetry signal comparison

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class ComparisonPlotter:
    title: str = "Comparison Visualization"
    xlabel: str = "X"
    ylabel: str = "Y"

    def compare_laps(self, positions: np.ndarray, lap_data: dict):
        """
        Compare multiple lap speed profiles.
        lap_data: dict {label: speed_array}
        """
        plt.figure(figsize=(10, 4))
        for label, speeds in lap_data.items():
            plt.plot(positions, speeds * 3.6, label=label)

        plt.xlabel(self.xlabel)
        plt.ylabel("Speed (km/h)")
        plt.title(f"{self.title} — Lap Comparison")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def compare_aero(self, velocities: np.ndarray, aero_data: dict):
        """
        Compare aerodynamic forces.
        aero_data: dict {label: force_array}
        """
        plt.figure(figsize=(10, 4))
        for label, forces in aero_data.items():
            plt.plot(velocities, forces, label=label)

        plt.xlabel(self.xlabel)
        plt.ylabel("Force (N)")
        plt.title(f"{self.title} — Aerodynamic Comparison")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def compare_telemetry(self, t: np.ndarray, signals: dict):
        """
        Compare multiple telemetry signals.
        signals: dict {label: signal_array}
        """
        plt.figure(figsize=(10, 4))
        for label, sig in signals.items():
            plt.plot(t, sig, label=label)

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(f"{self.title} — Telemetry Comparison")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


# Example usage

if __name__ == "__main__":
    t = np.linspace(0, 10, 500)
    s1 = np.sin(t)
    s2 = np.sin(t + 0.5)
    s3 = np.sin(t + 1.0)

    plotter = ComparisonPlotter(title="Demo Comparison", xlabel="Time (s)", ylabel="Signal")
    plotter.compare_telemetry(t, {"Lap 1": s1, "Lap 2": s2, "Lap 3": s3})
