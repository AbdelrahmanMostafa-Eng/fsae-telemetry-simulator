# test_vehicle.py

"""
Unit tests for simulation/vehicle.py

Tests:
- Drag force increases with speed
- Acceleration decreases with speed
- Acceleration is positive at low speed
- Acceleration approaches zero at high speed

"""

import numpy as np
from simulation.vehicle import Vehicle


def test_drag_increases_with_speed():
    car = Vehicle()
    drag_low = car.drag_force(10)
    drag_high = car.drag_force(30)
    assert drag_high > drag_low


def test_acceleration_decreases_with_speed():
    car = Vehicle()
    a_low = car.acceleration(5)
    a_high = car.acceleration(40)
    assert a_low > a_high


def test_acceleration_positive_at_low_speed():
    car = Vehicle()
    a = car.acceleration(1)
    assert a > 0


def test_acceleration_near_zero_at_high_speed():
    car = Vehicle()
    a = car.acceleration(80)
    assert a < 0.5
