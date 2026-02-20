# test_telemetry_tools.py

import numpy as np
from telemetry_tools import TelemetryTools


def test_smoothing_reduces_noise():
    t = np.linspace(0, 10, 200)
    noisy = np.sin(t) + np.random.normal(0, 0.5, len(t))

    tools = TelemetryTools(smoothing_window=10)
    smooth = tools.smooth(noisy)

    assert np.std(smooth) < np.std(noisy)


def test_differentiation_output_length():
    t = np.linspace(0, 10, 200)
    signal = np.sin(t)

    tools = TelemetryTools()
    deriv = tools.differentiate(signal, dt=t[1] - t[0])

    assert len(deriv) == len(signal)
