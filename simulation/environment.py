# environment.py

"""
Module for modeling environmental conditions for the FSAE Telemetry Simulator.

This version supports:
- Air temperature
- Track grip level
- Wind speed and direction
- Air density calculation from temperature

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Environment:
    temperature: float = 25.0      # °C
    wind_speed: float = 0.0        # m/s
    wind_direction: float = 0.0    # degrees (0 = headwind)
    grip: float = 1.0              # 1.0 = normal grip

    def air_density(self) -> float:
        """
        Calculate air density (kg/m³) using a simplified formula.
        """
        temp_k = self.temperature + 273.15
        return 1.225 * (273.15 / temp_k)

    def wind_effect(self, vehicle_speed: float) -> float:
        """
        Compute effective speed considering headwind/tailwind.
        Positive wind_direction = headwind.
        """
        return vehicle_speed + self.wind_speed * np.cos(np.radians(self.wind_direction))


# Example usage and plotting

if __name__ == "__main__":
    env = Environment(temperature=25, wind_speed=3, wind_direction=0)

    print("Environment Example:")
    print(f"Temperature: {env.temperature} °C")
    print(f"Air density: {env.air_density():.3f} kg/m³")
    print(f"Effective speed at 20 m/s: {env.wind_effect(20):.2f} m/s")

    # Plot air density vs temperature
    temps = np.linspace(-10, 40, 100)
    densities = [Environment(t).air_density() for t in temps]

    plt.figure(figsize=(8, 4))
    plt.plot(temps, densities, label="Air Density")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Air Density (kg/m³)")
    plt.title("Air Density vs Temperature")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
