# track.py

"""
Module for modeling a simple racing track for the FSAE Telemetry Simulator.

This version supports:
- Straight segments
- Corner segments with radius
- Total track length calculation
- Example usage with plotting of track layout (top‑down view)

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class TrackSegment:
    length: float              # meters
    segment_type: str          # "straight" or "corner"
    radius: float = None       # meters (only for corners)
    direction: int = 1         # +1 = left, -1 = right (for corners)


@dataclass
class Track:
    segments: list

    def total_length(self) -> float:
        """Return total track length in meters."""
        return sum(seg.length for seg in self.segments)

    def generate_xy(self):
        """
        Generate a simple 2D top‑down layout of the track.

        Returns:
            x, y arrays representing the track path.
        """
        x = [0.0]
        y = [0.0]
        heading = 0.0  # radians

        for seg in self.segments:
            if seg.segment_type == "straight":
                # Move forward in the current heading
                dx = seg.length * np.cos(heading)
                dy = seg.length * np.sin(heading)
                x.append(x[-1] + dx)
                y.append(y[-1] + dy)

            elif seg.segment_type == "corner":
                # Approximate corner with small steps
                steps = 50
                arc = seg.length / seg.radius
                angles = np.linspace(0, arc, steps) * seg.direction

                for a in angles:
                    heading += a / steps
                    dx = (seg.radius / steps) * np.cos(heading)
                    dy = (seg.radius / steps) * np.sin(heading)
                    x.append(x[-1] + dx)
                    y.append(y[-1] + dy)

        return np.array(x), np.array(y)


# Example usage and plotting

if __name__ == "__main__":
    # Build a simple track: straight → left corner → straight
    track = Track([
        TrackSegment(length=80, segment_type="straight"),
        TrackSegment(length=40, segment_type="corner", radius=20, direction=1),
        TrackSegment(length=60, segment_type="straight"),
    ])

    print("Track Example:")
    print(f"Total track length: {track.total_length():.1f} m")

    # Generate layout
    x, y = track.generate_xy()

    # Plot track layout
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Track Layout")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.title("Simple FSAE Track Layout")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
