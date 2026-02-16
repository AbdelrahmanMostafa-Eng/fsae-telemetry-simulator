# simulator.py

"""

Simple standalone simulator for straight‑line acceleration.

Uses:
- dataclass for configuration
- numpy for numerical simulation
- matplotlib for plotting

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class SimpleSimulator:
    mass: float = 230.0            # kg
    power: float = 80_000.0        # W
    drag_coeff: float = 0.9        # Cd
    frontal_area: float = 1.2      # m²
    rho: float = 1.225             # air density
    duration: float = 10.0         # seconds
    dt: float = 0.1                # timestep

    def drag_force(self, speed: float) -> float:
        """Aerodynamic drag force (N)."""
        return 0.5 * self.rho * self.drag_coeff * self.frontal_area * speed**2

    def acceleration(self, speed: float) -> float:
        """Compute acceleration at a given speed."""
        wheel_force = self.power / max(speed, 1e-3)
        net_force = wheel_force - self.drag_force(speed)
        return net_force / self.mass

    def run(self):
        """Run the simulation and return time, speed, distance arrays."""
        steps = int(self.duration / self.dt) + 1

        t = np.linspace(0, self.duration, steps)
        v = np.zeros(steps)
        x = np.zeros(steps)

        for i in range(1, steps):
            a = self.acceleration(v[i - 1])
            v[i] = v[i - 1] + a * self.dt
            v[i] = max(v[i], 0.0)
            x[i] = x[i - 1] + v[i] * self.dt

        return t, v, x


# Example usage and plotting

if __name__ == "__main__":
    sim = SimpleSimulator(duration=12.0, dt=0.1)
    t, v, x = sim.run()

    # Print outputs
    print("Straight-Line Simulation Example:")
    print(f"Final speed: {v[-1]:.2f} m/s ({v[-1] * 3.6:.1f} km/h)")
    print(f"Distance covered: {x[-1]:.1f} m")

    # Plot speed vs time
    plt.figure(figsize=(8, 4))
    plt.plot(t, v * 3.6, label="Speed (km/h)")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (km/h)")
    plt.title("Straight-Line Acceleration Simulation")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
