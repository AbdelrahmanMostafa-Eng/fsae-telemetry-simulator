# aero_map.py

"""
Module for generating aerodynamic maps for a race car.
Provides:
- Drag force vs speed
- Downforce vs speed
- Simple aerodynamic model using Cd, Cl, and frontal area

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class AeroMap:
    cd: float            # Drag coefficient
    cl: float            # Lift coefficient (negative for downforce)
    area: float          # Frontal area (m²)
    rho: float = 1.225   # Air density (kg/m³)

    def drag_force(self, velocity: float) -> float:
        """Aerodynamic drag force (N)."""
        return 0.5 * self.rho * self.cd * self.area * velocity**2

    def downforce(self, velocity: float) -> float:
        """Aerodynamic downforce (N)."""
        return 0.5 * self.rho * self.cl * self.area * velocity**2


# Example usage and plotting

if __name__ == "__main__":
    aero = AeroMap(cd=0.95, cl=3.2, area=1.5)

    velocities = np.linspace(20, 100, 60)  # m/s
    drag = [aero.drag_force(v) for v in velocities]
    df = [aero.downforce(v) for v in velocities]

    # Print sample values
    print("Aero Map Example:")
    for v in [30, 50, 70]:
        print(f"Speed {v} m/s → Drag = {aero.drag_force(v):.1f} N, Downforce = {aero.downforce(v):.1f} N")

    # Plot
    plt.plot(velocities, drag, label="Drag Force")
    plt.plot(velocities, df, label="Downforce")
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Force (N)")
    plt.title("Aerodynamic Map: Drag & Downforce vs Speed")
    plt.grid(True)
    plt.legend()
    plt.show()
