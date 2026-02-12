#export.py

"""

Module for exporting telemetry data to CSV or JSON.

"""

import csv
import json

class TelemetryExport:

    @staticmethod
    def to_csv(filename, laps, lap_times, speeds, fuel_use, tire_wear):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Lap", "Lap Time (s)", "Speed (km/h)", "Fuel Used (L)", "Tire Wear"])
            for i in range(len(laps)):
                writer.writerow([laps[i], lap_times[i], speeds[i], fuel_use[i], tire_wear[i]])

    @staticmethod
    def to_json(filename, laps, lap_times, speeds, fuel_use, tire_wear):
        data = [
            {"Lap": int(laps[i]), "Lap Time": float(lap_times[i]), "Speed": float(speeds[i]),
             "Fuel Used": float(fuel_use[i]), "Tire Wear": float(tire_wear[i])}
            for i in range(len(laps))
        ]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


# Example usage

if __name__ == "__main__":
    import numpy as np
    laps = np.arange(1, 6)
    lap_times = np.random.normal(75, 2, 5)
    speeds = np.random.normal(140, 5, 5)
    fuel_use = np.linspace(0, 5, 5)
    tire_wear = np.linspace(0, 0.2, 5)

    print("Telemetry Export Example:")
    TelemetryExport.to_csv("telemetry.csv", laps, lap_times, speeds, fuel_use, tire_wear)
    TelemetryExport.to_json("telemetry.json", laps, lap_times, speeds, fuel_use, tire_wear)
    print("Data exported to telemetry.csv and telemetry.json")
