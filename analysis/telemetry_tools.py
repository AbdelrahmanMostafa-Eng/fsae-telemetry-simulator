# telemetry_tools.py

"""
Module for basic telemetry processing and visualization.
Provides:
- Signal smoothing
- Numerical differentiation
- Basic statistics
- Example usage with plotting

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class TelemetryTools:
    smoothing_window: int = 5

    def smooth(self, signal: np.ndarray) -> np.ndarray:
        """Apply simple moving average smoothing."""
        window = self.smoothing_window
        if window < 2:
            return signal
        kernel = np.ones(window) / window
        return np.convolve(signal, kernel, mode="same")

    def differentiate(self, signal: np.ndarray, dt: float) -> np.ndarray:
        """Numerical derivative using central differences."""
        deriv = np.zeros_like(signal)
        deriv[1:-1] = (signal[2:] - signal[:-2]) / (2 * dt)
        deriv[0] = deriv[1]
        deriv[-1] = deriv[-2]
        return deriv

    def stats(self, signal: np.ndarray) -> dict:
        """Return basic statistics for a signal."""
        return {
            "min": float(np.min(signal)),
            "max": float(np.max(signal)),
            "mean": float(np.mean(signal)),
            "std": float(np.std(signal)),
        }


# Example usage and plotting

if __name__ == "__main__":
    t = np.linspace(0, 10, 500)
    raw_speed = 20 + 5 * np.sin(2 * np.pi * 0.5 * t) + np.random.normal(0, 0.8, len(t))

    tools = TelemetryTools(smoothing_window=15)
    smooth_speed = tools.smooth(raw_speed)
    accel = tools.differentiate(smooth_speed, dt=t[1] - t[0])

    print("Telemetry Statistics:")
    print(tools.stats(smooth_speed))

    plt.figure(figsize=(10, 5))
    plt.plot(t, raw_speed, alpha=0.4, label="Raw Speed")
    plt.plot(t, smooth_speed, label="Smoothed Speed")
    plt.plot(t, accel, label="Acceleration")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed / Acceleration")
    plt.title("Telemetry Processing Example")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
