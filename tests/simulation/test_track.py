# test_track.py

"""
Unit tests for simulation/track.py

Tests:
- Total track length is computed correctly
- generate_xy returns valid coordinate arrays
- Corner direction affects the XY path
"""

import numpy as np
from simulation.track import Track, TrackSegment


def test_track_length():
    track = Track([
        TrackSegment(50, "straight"),
        TrackSegment(30, "corner", radius=15, direction=1),
        TrackSegment(20, "straight"),
    ])
    assert track.total_length() == 100


def test_generate_xy_returns_arrays():
    track = Track([
        TrackSegment(80, "straight"),
        TrackSegment(40, "corner", radius=20, direction=1),
    ])
    x, y = track.generate_xy()

    assert isinstance(x, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert len(x) == len(y)
    assert len(x) > 2  # should generate multiple points


def test_corner_direction_changes_path():
    # Left corner
    track_left = Track([
        TrackSegment(50, "straight"),
        TrackSegment(30, "corner", radius=15, direction=1),
    ])
    x_left, y_left = track_left.generate_xy()

    # Right corner
    track_right = Track([
        TrackSegment(50, "straight"),
        TrackSegment(30, "corner", radius=15, direction=-1),
    ])
    x_right, y_right = track_right.generate_xy()

    # After the corner, Y should differ in sign
    assert np.sign(y_left[-1]) != np.sign(y_right[-1])
