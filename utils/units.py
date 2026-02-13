#units.py

"""

Unit conversion helpers for the FSAE Telemetry Simulator.
These functions keep calculations clean and consistent.

"""

def kmh_to_ms(kmh: float) -> float:
    """Convert km/h to m/s."""
    return kmh / 3.6


def ms_to_kmh(ms: float) -> float:
    """Convert m/s to km/h."""
    return ms * 3.6


def kg_to_lbs(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg * 2.20462


def lbs_to_kg(lbs: float) -> float:
    """Convert pounds to kilograms."""
    return lbs / 2.20462
