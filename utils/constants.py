#constants.py

"""

Global constants used across the FSAE Telemetry Simulator.
These values can be tuned to match a specific car or event.

"""

# Track & lap
LAP_LENGTH_M = 1200.0          # meters per lap (example FSAE track length)
SECTOR_COUNT = 3               # number of sectors per lap

# Pit stop
PIT_STOP_TIME_S = 7.5          # seconds for a standard pit stop

# Fuel
FUEL_DENSITY_KG_PER_L = 0.75   # approximate density of race fuel
FUEL_TANK_CAPACITY_L = 20.0    # liters

# Tires
BASE_TIRE_WEAR_RATE = 0.05     # wear per lap (0–1 scale)
MAX_TIRE_WEAR = 1.0            # fully worn
