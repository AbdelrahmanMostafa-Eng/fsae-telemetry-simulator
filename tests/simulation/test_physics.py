# test_physics.py

"""
Unit tests for simulation/physics.py

Tests:
- Drag force increases with speed
- Rolling resistance is constant
- Acceleration decreases with speed
- Acceleration becomes very small at high speed

"""

import numpy as np
from simulation.physics import PhysicsModel


def test_drag_increases_with_speed():
    model = PhysicsModel()
    drag_low = model.drag_force(10)
    drag_high = model.drag_force(30)
    assert drag_high > drag_low


def test_rolling_resistance_constant():
    model = PhysicsModel()
    rr1 = model.rolling_resistance()
    rr2 = model.rolling_resistance()
    assert rr1 == rr2


def test_acceleration_decreases_with_speed():
    model = PhysicsModel()
    a_low = model.acceleration(5)
    a_high = model.acceleration(40)
    assert a_low > a_high


def test_acceleration_near_zero_at_high_speed():
    model = PhysicsModel()
    a = model.acceleration(80)  # ~288 km/h
    assert a < 0.5
