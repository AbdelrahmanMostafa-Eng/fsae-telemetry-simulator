# test_environment.py

"""
Unit tests for simulation/environment.py

Tests:
- Air density decreases as temperature increases
- Wind effect increases speed with headwind
- Wind effect decreases speed with tailwind
"""

import numpy as np
from simulation.environment import Environment


def test_air_density_decreases_with_temperature():
    cold = Environment(temperature=0).air_density()
    hot = Environment(temperature=40).air_density()
    assert hot < cold


def test_wind_effect_headwind_increases_effective_speed():
    env = Environment(wind_speed=5, wind_direction=0)  # headwind
    effective = env.wind_effect(20)
    assert effective > 20


def test_wind_effect_tailwind_decreases_effective_speed():
    env = Environment(wind_speed=5, wind_direction=180)  # tailwind
    effective = env.wind_effect(20)
    assert effective < 20
