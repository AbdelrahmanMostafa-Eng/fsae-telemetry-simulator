#test_analysis.py

"""
Unit tests for telemetry.analysis.
"""

import numpy as np
from telemetry.analysis import TelemetryAnalysis


def test_average_lap_time():
    laps = np.array([60.0, 62.0, 61.0, 63.0])
    avg = TelemetryAnalysis.average_lap_time(laps)
    assert avg == np.mean(laps)


def test_compare_stints_faster_first():
    stint1 = np.array([60, 61, 62])
    stint2 = np.array([65, 66, 67])

    result = TelemetryAnalysis.compare_stints(stint1, stint2)
    assert result == "stint1"


def test_compare_stints_faster_second():
    stint1 = np.array([70, 72, 71])
    stint2 = np.array([65, 66, 67])

    result = TelemetryAnalysis.compare_stints(stint1, stint2)
    assert result == "stint2"


def test_compare_stints_equal():
    stint1 = np.array([60, 60, 60])
    stint2 = np.array([60, 60, 60])

    result = TelemetryAnalysis.compare_stints(stint1, stint2)
    assert result == "equal"
