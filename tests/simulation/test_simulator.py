# test_simulator.py

"""
Unit tests for simulation/simulator.py

Tests:
- Simulation returns arrays of correct length
- Speed is always non-negative
- Distance increases monotonically
"""

import numpy as np
from simulation.simulator import SimpleSimulator


def test_simulation_output_shapes():
    sim = SimpleSimulator(duration=10, dt=0.1)
    t, v, x = sim.run()

    assert isinstance(t, np.ndarray)
    assert isinstance(v, np.ndarray)
    assert isinstance(x, np.ndarray)

    assert len(t) == len(v) == len(x)
    assert len(t) > 5  # should have multiple steps


def test_speed_non_negative():
    sim = SimpleSimulator(duration=10, dt=0.1)
    _, v, _ = sim.run()

    assert np.all(v >= 0)


def test_distance_monotonic():
    sim = SimpleSimulator(duration=10, dt=0.1)
    _, _, x = sim.run()

    # Distance should never decrease
    diffs = np.diff(x)
    assert np.all(diffs >= 0)
