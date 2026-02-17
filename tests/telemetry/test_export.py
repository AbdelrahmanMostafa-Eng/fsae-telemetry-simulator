#test_export.py

"""
Unit tests for telemetry.export.
"""

import os
import json
import csv
import numpy as np
from telemetry.export import TelemetryExport


def test_to_csv(tmp_path):
    filename = tmp_path / "test_output.csv"

    laps = np.array([1, 2, 3])
    lap_times = np.array([60.0, 61.0, 62.0])
    speeds = np.array([120.0, 121.0, 122.0])
    fuel_use = np.array([0.5, 1.0, 1.5])
    tire_wear = np.array([0.01, 0.02, 0.03])

    TelemetryExport.to_csv(filename, laps, lap_times, speeds, fuel_use, tire_wear)

    assert filename.exists()

    with open(filename, "r") as f:
        reader = list(csv.reader(f))
        assert len(reader) == 4  # header + 3 rows
        assert reader[0] == ["Lap", "Lap Time (s)", "Speed (km/h)", "Fuel Used (L)", "Tire Wear"]


def test_to_json(tmp_path):
    filename = tmp_path / "test_output.json"

    laps = np.array([1, 2, 3])
    lap_times = np.array([60.0, 61.0, 62.0])
    speeds = np.array([120.0, 121.0, 122.0])
    fuel_use = np.array([0.5, 1.0, 1.5])
    tire_wear = np.array([0.01, 0.02, 0.03])

    TelemetryExport.to_json(filename, laps, lap_times, speeds, fuel_use, tire_wear)

    assert filename.exists()

    with open(filename, "r") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]["Lap"] == 1
    assert data[0]["Lap Time"] == 60.0
    assert data[0]["Speed"] == 120.0


if __name__ == "__main__":
    print("Running TelemetryExport tests...\n")

    tests = [
        ("test_to_csv", lambda: test_to_csv(__import__("pathlib").Path("."))),
        ("test_to_json", lambda: test_to_json(__import__("pathlib").Path("."))),
    ]

    for name, func in tests:
        try:
            func()
            print(f"✔ {name} passed")
        except Exception:
            print(f"✘ {name} FAILED")

    print("\nAll tests completed.")
