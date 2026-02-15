#test_generator.py

"""
Unit tests for TelemetryGenerator.
"""

import numpy as np
from telemetry.generator import TelemetryGenerator


def test_generate_shapes():
    gen = TelemetryGenerator(laps=20, max_speed=140, fuel_capacity=20)
    lap_times, speeds, fuel_use, tire_wear = gen.generate()

    assert len(lap_times) == 20
    assert len(speeds) == 20
    assert len(fuel_use) == 20
    assert len(tire_wear) == 20


def test_fuel_is_non_decreasing():
    gen = TelemetryGenerator(laps=15, max_speed=130, fuel_capacity=15)
    _, _, fuel_use, _ = gen.generate()

    assert np.all(np.diff(fuel_use) >= 0)


def test_tire_wear_is_non_decreasing():
    gen = TelemetryGenerator(laps=15, max_speed=130, fuel_capacity=15)
    _, _, _, tire_wear = gen.generate()

    assert np.all(np.diff(tire_wear) >= 0)


def test_speeds_within_reasonable_range():
    gen = TelemetryGenerator(laps=10, max_speed=140, fuel_capacity=10)
    _, speeds, _, _ = gen.generate()

    assert np.all(speeds >= 0)
    assert np.all(speeds <= 200)


if __name__ == "__main__":
    print("Running TelemetryGenerator tests...\n")

    tests = [
        ("test_generate_shapes", test_generate_shapes),
        ("test_fuel_is_non_decreasing", test_fuel_is_non_decreasing),
        ("test_tire_wear_is_non_decreasing", test_tire_wear_is_non_decreasing),
        ("test_speeds_within_reasonable_range", test_speeds_within_reasonable_range),
    ]

    for name, func in tests:
        try:
            func()
            print(f"✔ {name} passed")
        except AssertionError:
            print(f"✘ {name} FAILED")

    print("\nAll tests completed.")
