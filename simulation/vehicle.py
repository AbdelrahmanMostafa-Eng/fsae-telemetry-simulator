# vehicle.py

"""
Module for modeling a simple FSAE-style vehicle.

Includes:
- Basic vehicle parameters (mass, power, aero)
- Simple acceleration model
- Example usage with plotting

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Vehicle:
    mass: float = 230.0          # kg
    power: float = 80_000.0      # W
    drag_coeff: float = 0.9      # Cd
    frontal_area: float = 1.2    # m²
    rho: float = 1.225           # air density (kg/m³)

    def drag_force(self, speed: float) -> float:
        """Aerodynamic drag force (N)."""
        return 0.5 * self.rho * self.drag_coeff * self.frontal_area * speed**2

    def acceleration(self, speed: float) -> float:
        """Compute acceleration at a given speed."""
        wheel_force = self.power / max(speed, 1e-3)
        net_force = wheel_force - self.drag_force(speed)
        return net_force / self.mass


# Example usage and plotting

if __name__ == "__main__":
    car = Vehicle()

    speeds_kmh = np.linspace(0, 160, 60)
    speeds_ms = speeds_kmh / 3.6

    accels = [car.acceleration(v) for v in speeds_ms]

    print("=== Vehicle Example ===")
    for v in [20, 60, 100]:
        print(f"Acceleration at {v} km/h → {car.acceleration(v/3.6):.2f} m/s²")

    plt.figure(figsize=(8, 4))
    plt.plot(speeds_kmh, accels, label="Acceleration (m/s²)")
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Acceleration (m/s²)")
    plt.title("Vehicle Acceleration vs Speed")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
