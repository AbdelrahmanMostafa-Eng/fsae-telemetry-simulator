# example_usages.py

"""
Integration demo for simulation modules:
- vehicle.py
- physics.py
- environment.py
- track.py
- simulator.py
"""

import numpy as np
import matplotlib.pyplot as plt

from simulation.vehicle import Vehicle
from simulation.physics import PhysicsModel
from simulation.environment import Environment
from simulation.track import Track, TrackSegment
from simulation.simulator import SimpleSimulator


# ---------------------------------------------------------
# DATA GENERATION
# ---------------------------------------------------------

# Speed range (km/h → m/s)
velocities = np.linspace(0, 160, 60)
vel_ms = velocities / 3.6

# Vehicle & physics
vehicle = Vehicle()
physics = PhysicsModel()

drag_forces = [physics.drag_force(v) for v in vel_ms]
accelerations = [physics.acceleration(v) for v in vel_ms]

# Environment
temps = np.linspace(-10, 40, 60)
air_densities = [Environment(t).air_density() for t in temps]

# Track
track = Track([
    TrackSegment(80, "straight"),
    TrackSegment(40, "corner", radius=20, direction=1),
    TrackSegment(60, "straight"),
])
x, y = track.generate_xy()

# Simulator
sim = SimpleSimulator(duration=12, dt=0.1)
t, v, dist = sim.run()


# ---------------------------------------------------------
# PRINT SAMPLE OUTPUTS
# ---------------------------------------------------------

print("=== Simulation Integration Example ===")
print(f"Drag at 100 km/h → {physics.drag_force(100/3.6):.1f} N")
print(f"Acceleration at 80 km/h → {physics.acceleration(80/3.6):.2f} m/s²")
print(f"Air density at 25°C → {Environment(25).air_density():.3f} kg/m³")
print(f"Track length → {track.total_length():.1f} m")
print(f"Final speed after 12 s → {v[-1]*3.6:.1f} km/h")


# ---------------------------------------------------------
# PLOTTING (4‑panel layout)
# ---------------------------------------------------------

plt.figure(figsize=(12, 8))

# 1. Drag vs Speed
plt.subplot(2, 2, 1)
plt.plot(velocities, drag_forces, label="Drag Force", color="red")
plt.xlabel("Speed (km/h)")
plt.ylabel("Drag (N)")
plt.title("Drag vs Speed")
plt.grid(True)
plt.legend()

# 2. Acceleration vs Speed
plt.subplot(2, 2, 2)
plt.plot(velocities, accelerations, label="Acceleration", color="blue")
plt.xlabel("Speed (km/h)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration vs Speed")
plt.grid(True)
plt.legend()

# 3. Air Density vs Temperature
plt.subplot(2, 2, 3)
plt.plot(temps, air_densities, label="Air Density", color="green")
plt.xlabel("Temperature (°C)")
plt.ylabel("Air Density (kg/m³)")
plt.title("Air Density vs Temperature")
plt.grid(True)
plt.legend()

# 4. Track Layout
plt.subplot(2, 2, 4)
plt.plot(x, y, label="Track Layout", color="purple")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Track Layout")
plt.axis("equal")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
