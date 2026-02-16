# physics.py

"""
Physics helper module for the FSAE Telemetry Simulator.

Includes:
- Aerodynamic drag force
- Rolling resistance
- Power‑limited acceleration
- Example usage with plotting

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class PhysicsModel:
    rho: float = 1.225            # air density (kg/m³)
    drag_coeff: float = 0.9       # Cd
    frontal_area: float = 1.2     # m²
    mass: float = 230.0           # kg
    c_rr: float = 0.015           # rolling resistance coefficient
    power: float = 80_000.0       # W

    def drag_force(self, speed: float) -> float:
        """Aerodynamic drag force (N)."""
        return 0.5 * self.rho * self.drag_coeff * self.frontal_area * speed**2

    def rolling_resistance(self) -> float:
        """Rolling resistance force (N)."""
        return self.c_rr * self.mass * 9.81

    def acceleration(self, speed: float) -> float:
        """
        Compute acceleration at a given speed using:
        - power‑limited wheel force
        - drag
        - rolling resistance
        """
        wheel_force = self.power / max(speed, 1e-3)
        net_force = wheel_force - self.drag_force(speed) - self.rolling_resistance()
        return net_force / self.mass


# Example usage and plotting

if __name__ == "__main__":
    model = PhysicsModel()

    # Speed range (km/h → m/s)
    speeds_kmh = np.linspace(0, 160, 80)
    speeds_ms = speeds_kmh / 3.6

    drag = [model.drag_force(v) for v in speeds_ms]
    accel = [model.acceleration(v) for v in speeds_ms]

    # Print example outputs
    print("Physics Model Example:")
    for v in [20, 60, 100]:
        v_ms = v / 3.6
        print(f"Speed {v:3d} km/h → Drag = {model.drag_force(v_ms):.1f} N, Accel = {model.acceleration(v_ms):.2f} m/s²")

    # Plot drag force and acceleration
    plt.figure(figsize=(8, 4))
    plt.plot(speeds_kmh, drag, label="Drag Force (N)")
    plt.plot(speeds_kmh, accel, label="Acceleration (m/s²)")
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Force / Acceleration")
    plt.title("Drag Force & Acceleration vs Speed")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
