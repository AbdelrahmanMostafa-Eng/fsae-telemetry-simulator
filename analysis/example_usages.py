# example_usages.py

"""
Integration demo for analysis modules:
- lap_simulator.py
- cornering_model.py
- aero_map.py
- telemetry_tools.py
- plotting.py
"""

import numpy as np
import matplotlib.pyplot as plt

from lap_simulator import SimplePhysics, SimpleTrack, TrackSegment, LapSimulator
from cornering_model import CorneringModel
from aero_map import AeroMap
from telemetry_tools import TelemetryTools


# ---------------------------------------------------------
# Lap Simulation
# ---------------------------------------------------------

physics = SimplePhysics(
    mass=230.0,
    power=80_000.0,
    drag_coeff=0.9,
    frontal_area=1.2
)

track = SimpleTrack([
    TrackSegment(100, "straight"),
    TrackSegment(40, "corner", radius=25),
    TrackSegment(120, "straight"),
    TrackSegment(30, "corner", radius=18),
])

lap_sim = LapSimulator(physics, track)
pos, speeds, lap_time = lap_sim.run()


# ---------------------------------------------------------
# Cornering Model
# ---------------------------------------------------------

corner_model = CorneringModel(
    mass=230.0,
    mu=1.8,
    downforce_coeff=12.0
)

radii = np.linspace(10, 200, 80)
corner_speeds = [corner_model.cornering_speed(r) for r in radii]


# ---------------------------------------------------------
# Aero Map
# ---------------------------------------------------------

aero = AeroMap(cd=0.95, cl=3.2, area=1.5)
velocities = np.linspace(20, 100, 60)
drag = [aero.drag_force(v) for v in velocities]
downforce = [aero.downforce(v) for v in velocities]


# ---------------------------------------------------------
# Telemetry Tools
# ---------------------------------------------------------

t = np.linspace(0, 10, 500)
raw_signal = 20 + 5 * np.sin(2 * np.pi * 0.5 * t) + np.random.normal(0, 0.8, len(t))

tools = TelemetryTools(smoothing_window=15)
smooth_signal = tools.smooth(raw_signal)
accel = tools.differentiate(smooth_signal, dt=t[1] - t[0])


# ---------------------------------------------------------
# Print sample outputs
# ---------------------------------------------------------

print("=== Analysis Integration Example ===")
print(f"Lap time → {lap_time:.2f} s")
print(f"Max lap speed → {np.max(speeds) * 3.6:.1f} km/h")
print(f"Cornering speed at 50 m radius → {corner_model.cornering_speed(50) * 3.6:.1f} km/h")
print(f"Drag at 60 m/s → {aero.drag_force(60):.1f} N")
print(f"Smoothed signal mean → {tools.stats(smooth_signal)['mean']:.2f}")


# ---------------------------------------------------------
# Plotting
# ---------------------------------------------------------

plt.figure(figsize=(12, 8))

# Lap speed profile
plt.subplot(2, 2, 1)
plt.plot(pos, speeds * 3.6)
plt.xlabel("Track Position (units)")
plt.ylabel("Speed (km/h)")
plt.title("Lap Speed Profile")

# Cornering speed vs radius
plt.subplot(2, 2, 2)
plt.plot(radii, np.array(corner_speeds) * 3.6)
plt.xlabel("Corner Radius (m)")
plt.ylabel("Speed (km/h)")
plt.title("Cornering Speed vs Radius")

# Aero map
plt.subplot(2, 2, 3)
plt.plot(velocities, drag, label="Drag")
plt.plot(velocities, downforce, label="Downforce")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Force (N)")
plt.title("Aero Map")
plt.legend()

# Telemetry processing
plt.subplot(2, 2, 4)
plt.plot(t, raw_signal, alpha=0.4, label="Raw")
plt.plot(t, smooth_signal, label="Smoothed")
plt.plot(t, accel, label="Acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Signal")
plt.title("Telemetry Processing")
plt.legend()

plt.tight_layout()
plt.show()
