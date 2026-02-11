#generator.py

"""

Synthetic telemetry generator for FSAE laps/sessions.
Produces lap times, speeds, fuel usage, and tire wear traces.

"""

from dataclasses import dataclass
import numpy as np

@dataclass
class TelemetryGenerator:
    laps: int
    max_speed: float      # km/h
    fuel_capacity: float  # liters

    def generate(self):
        """Generate synthetic telemetry arrays for a session."""
        lap_times = np.random.normal(75, 2, self.laps)
        speeds = np.random.normal(self.max_speed*0.8, 10, self.laps)
        fuel_use = np.linspace(0, self.fuel_capacity, self.laps)
        tire_wear = np.linspace(0, 1, self.laps)
        return lap_times, speeds, fuel_use, tire_wear


# Example usage

if __name__ == "__main__":
    gen = TelemetryGenerator(laps=20, max_speed=140, fuel_capacity=20)
    lap_times, speeds, fuel_use, tire_wear = gen.generate()

    print("Telemetry Generator Example:")
    print(f"Lap Times (first 5) → {lap_times[:5]}")
    print(f"Speeds (first 5) → {speeds[:5]}")
    print(f"Fuel Used Final → {fuel_use[-1]:.1f} L")
    print(f"Tire Wear Final → {tire_wear[-1]:.2f}")
