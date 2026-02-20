# test_lap_simulator.py

import numpy as np
from lap_simulator import SimplePhysics, SimpleTrack, TrackSegment, LapSimulator


def test_lap_simulator_shapes():
    physics = SimplePhysics(230, 80000, 0.9, 1.2)
    track = SimpleTrack([
        TrackSegment(100, "straight"),
        TrackSegment(40, "corner", radius=25),
    ])

    sim = LapSimulator(physics, track)
    pos, speeds, lap_time = sim.run()

    assert isinstance(pos, np.ndarray)
    assert isinstance(speeds, np.ndarray)
    assert len(pos) == len(speeds)
    assert lap_time > 0


def test_lap_speed_non_negative():
    physics = SimplePhysics(230, 80000, 0.9, 1.2)
    track = SimpleTrack([TrackSegment(100, "straight")])

    sim = LapSimulator(physics, track)
    _, speeds, _ = sim.run()

    assert np.all(speeds >= 0)
