# aero_plots.py

"""
Visualization utilities for aerodynamic analysis.
Provides:
- Drag vs speed plotting
- Downforce vs speed plotting
- Combined aerodynamic map visualization

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class AeroPlotter:
    title: str = "Aerodynamic Visualization"
    xlabel: str = "Velocity (m/s)"
    ylabel_drag: str = "Drag Force (N)"
    ylabel_downforce: str = "Downforce (N)"

    def plot_drag(self, velocities: np.ndarray, drag: np.ndarray):
        """Plot drag force vs speed."""
        plt.figure(figsize=(10, 4))
        plt.plot(velocities, drag, label="Drag", color="red")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel_drag)
        plt.title(f"{self.title} — Drag vs Speed")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_downforce(self, velocities: np.ndarray, downforce: np.ndarray):
        """Plot downforce vs speed."""
        plt.figure(figsize=(10, 4))
        plt.plot(velocities, downforce, label="Downforce", color="blue")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel_downforce)
        plt.title(f"{self.title} — Downforce vs Speed")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_aero_map(self, velocities: np.ndarray, drag: np.ndarray, downforce: np.ndarray):
        """Plot drag and downforce together."""
        plt.figure(figsize=(10, 5))
        plt.plot(velocities, drag, label="Drag", color="red")
        plt.plot(velocities, downforce, label="Downforce", color="blue")
        plt.xlabel(self.xlabel)
        plt.ylabel("Force (N)")
        plt.title(f"{self.title} — Aero Map")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


# Example usage

if __name__ == "__main__":
    v = np.linspace(20, 100, 60)
    drag = 0.5 * 1.225 * 1.0 * 1.5 * v**2
    downforce = 0.5 * 1.225 * 3.0 * 1.5 * v**2

    plotter = AeroPlotter(title="Demo Aero Map")
    plotter.plot_drag(v, drag)
    plotter.plot_downforce(v, downforce)
    plotter.plot_aero_map(v, drag, downforce)
