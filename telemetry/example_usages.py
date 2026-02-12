#example_usages.py

"""

Runs all modules inside the telemetry folder:
- generator
- plots
- analysis
- export

"""

import numpy as np

from generator import TelemetryGenerator
from plots import TelemetryPlots
from analysis import TelemetryAnalysis
from export import TelemetryExport


def main():
    print("=== Running Telemetry Folder ===")

    # --- Generate telemetry ---
    gen = TelemetryGenerator(laps=20, max_speed=140, fuel_capacity=20)
    lap_times, speeds, fuel_use, tire_wear = gen.generate()
    laps = np.arange(1, 21)

    print("\nGenerated Telemetry:")
    print(f"Lap Times (first 5): {lap_times[:5]}")
    print(f"Speeds (first 5): {speeds[:5]}")
    print(f"Final Fuel Used: {fuel_use[-1]:.1f} L")
    print(f"Final Tire Wear: {tire_wear[-1]:.2f}")

    # --- PLOTS (this is what you asked about) ---
    print("\nShowing Plots...")
    TelemetryPlots.plot_lap_times(laps, lap_times)
    TelemetryPlots.plot_fuel(laps, fuel_use)
    TelemetryPlots.plot_tire_wear(laps, tire_wear)

    # --- Analysis ---
    print("\nStint Comparison:")
    stint1 = np.random.normal(75, 2, 20)
    stint2 = np.random.normal(77, 2, 20)
    avg1, avg2, result = TelemetryAnalysis.compare_stints(stint1, stint2)

    print(f"Stint 1 Avg: {avg1:.2f} s")
    print(f"Stint 2 Avg: {avg2:.2f} s")
    print(f"Result: {result}")

    # --- Export ---
    TelemetryExport.to_csv("telemetry.csv", laps, lap_times, speeds, fuel_use, tire_wear)
    TelemetryExport.to_json("telemetry.json", laps, lap_times, speeds, fuel_use, tire_wear)

    print("\nExported telemetry.csv and telemetry.json")


if __name__ == "__main__":
    main()
