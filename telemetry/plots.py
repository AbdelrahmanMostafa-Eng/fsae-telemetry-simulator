#plots.py

"""

Module for visualizing telemetry data (lap times, fuel, tire wear, speed).

"""

import matplotlib.pyplot as plt

class TelemetryPlots:

    @staticmethod
    def plot_lap_times(laps, lap_times):
        plt.plot(laps, lap_times, color="blue")
        plt.xlabel("Lap")
        plt.ylabel("Lap Time (s)")
        plt.title("Lap Times")
        plt.show()

    @staticmethod
    def plot_fuel(laps, fuel_use):
        plt.plot(laps, fuel_use, color="green")
        plt.xlabel("Lap")
        plt.ylabel("Fuel Used (L)")
        plt.title("Fuel Consumption")
        plt.show()

    @staticmethod
    def plot_tire_wear(laps, tire_wear):
        plt.plot(laps, tire_wear, color="red")
        plt.xlabel("Lap")
        plt.ylabel("Tire Wear")
        plt.title("Tire Wear Progression")
        plt.show()


# Plotting

if __name__ == "__main__":
    import numpy as np
    laps = np.arange(1, 21)
    lap_times = np.random.normal(75, 2, 20)
    fuel_use = np.linspace(0, 20, 20)
    tire_wear = np.linspace(0, 1, 20)

    print("Telemetry Plots Example:")
    TelemetryPlots.plot_lap_times(laps, lap_times)
    TelemetryPlots.plot_fuel(laps, fuel_use)
    TelemetryPlots.plot_tire_wear(laps, tire_wear)
