# lap_simulator.py

"""
Independent module for estimating lap speed profiles using a simple physics model.
Provides:
- Power‑limited acceleration model
- Cornering speed model
- Track composed of straights and corners
- Example usage with a speed profile plot

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


# Simple Physics Model

@dataclass
class SimplePhysics:
    mass: float
    power: float
    drag_coeff: float
    frontal_area: float
    rho: float = 1.225

    def drag_force(self, speed: float) -> float:
        """Aerodynamic drag force (N)."""
        return 0.5 * self.rho * self.drag_coeff * self.frontal_area * speed**2

    def acceleration(self, speed: float) -> float:
        """Power‑limited acceleration (m/s²)."""
        wheel_force = self.power / max(speed, 1e-3)
        net_force = wheel_force - self.drag_force(speed)
        return net_force / self.mass


# Simple Track Model

@dataclass
class TrackSegment:
    length: float
    segment_type: str  # "straight" or "corner"
    radius: float = None


@dataclass
class SimpleTrack:
    segments: list

    def total_length(self) -> float:
        return sum(seg.length for seg in self.segments)


# Lap Simulator

@dataclass
class LapSimulator:
    physics: SimplePhysics
    track: SimpleTrack
    grip: float = 1.2
    dt: float = 0.1

    def corner_speed(self, radius: float) -> float:
        """Cornering speed using v = sqrt(mu * g * r)."""
        g = 9.81
        return np.sqrt(self.grip * g * radius)

    def run(self):
        """Simulate a lap and return position, speed, and lap time."""
        speeds = []
        positions = []
        total_time = 0.0
        v = 0.0

        for seg in self.track.segments:
            length = seg.length
            steps = int(length / (max(v, 1e-3) * self.dt)) + 1

            for _ in range(steps):
                if seg.segment_type == "straight":
                    v = max(v + self.physics.acceleration(v) * self.dt, 0)
                else:
                    v = min(v, self.corner_speed(seg.radius))

                speeds.append(v)
                positions.append(len(positions))
                total_time += self.dt

        return np.array(positions), np.array(speeds), total_time


# Example Usage and Plotting

if __name__ == "__main__":
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

    sim = LapSimulator(physics, track)
    pos, speeds, lap_time = sim.run()

    print("Lap Simulation Example:")
    print(f"Lap time: {lap_time:.2f} seconds")
    print(f"Max speed: {np.max(speeds) * 3.6:.1f} km/h")

    plt.plot(pos, speeds * 3.6, label="Speed (km/h)")
    plt.xlabel("Track Position (units)")
    plt.ylabel("Speed (km/h)")
    plt.title("Lap Speed Profile")
    plt.grid(True)
    plt.legend()
    plt.show()
