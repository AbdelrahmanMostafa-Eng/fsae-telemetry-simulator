#analysis.py

"""

Module for analyzing telemetry data.
Includes comparison of stints, drivers, and strategies.

"""

import numpy as np

class TelemetryAnalysis:

    @staticmethod
    def compare_stints(lap_times1, lap_times2):
        avg1 = np.mean(lap_times1)
        avg2 = np.mean(lap_times2)
        return avg1, avg2, "Stint 1 faster" if avg1 < avg2 else "Stint 2 faster"


# Example usage

if __name__ == "__main__":
    laps1 = np.random.normal(75, 2, 20)
    laps2 = np.random.normal(77, 2, 20)

    print("=== Telemetry Analysis Example ===")
    avg1, avg2, result = TelemetryAnalysis.compare_stints(laps1, laps2)
    print(f"Stint 1 Avg → {avg1:.2f} s")
    print(f"Stint 2 Avg → {avg2:.2f} s")
    print(f"Result → {result}")
