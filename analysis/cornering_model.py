# cornering_model.py

"""
Module for calculating cornering speed based on lateral grip.
Provides a simple model using:
- Tire friction coefficient (mu)
- Corner radius (m)
- Vehicle mass (kg)
- Aerodynamic downforce (optional)

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class CorneringModel:
    mass: float
    mu: float
    downforce_coeff: float = 0.0  # N per (m/s)²
    g: float = 9.81

    def normal_force(self, speed: float) -> float:
        """Total normal load = weight + aerodynamic load."""
        aero_load = self.downforce_coeff * speed**2
        return self.mass * self.g + aero_load

    def cornering_speed(self, radius: float, speed_guess: float = 30.0) -> float:
        """
        Solve v = sqrt( (mu * N) * r / m )
        Iterative because N depends on v (aero load).
        """
        v = speed_guess
        for _ in range(20):
            N = self.normal_force(v)
            v = np.sqrt((self.mu * N * radius) / self.mass)
        return v


# Example usage and plotting

if __name__ == "__main__":
    model = CorneringModel(
        mass=230.0,
        mu=1.8,
        downforce_coeff=12.0  # N per (m/s)²
    )

    radii = np.linspace(10, 200, 80)
    speeds = [model.cornering_speed(r) for r in radii]

    # Print sample outputs
    print("Cornering Speed Example:")
    for r in [20, 50, 100]:
        v = model.cornering_speed(r)
        print(f"Radius {r} m → Speed = {v*3.6:.1f} km/h")

    # Plot
    plt.plot(radii, np.array(speeds) * 3.6, label="Cornering Speed")
    plt.xlabel("Corner Radius (m)")
    plt.ylabel("Speed (km/h)")
    plt.title("Cornering Speed vs Radius")
    plt.grid(True)
    plt.legend()
    plt.show()
