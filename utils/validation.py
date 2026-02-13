#validation.py

"""

Input validation helpers for the FSAE Telemetry Simulator.
These functions help ensure clean, predictable data.

"""

def validate_positive(value, name="value"):
    """Ensure a numeric value is positive."""
    if value <= 0:
        raise ValueError(f"{name} must be positive, got {value}")


def validate_non_negative(value, name="value"):
    """Ensure a numeric value is zero or positive."""
    if value < 0:
        raise ValueError(f"{name} must be non-negative, got {value}")


def validate_array_length(arr, expected, name="array"):
    """Ensure an array has the expected length."""
    if len(arr) != expected:
        raise ValueError(f"{name} must have length {expected}, got {len(arr)}")


def validate_same_length(*arrays):
    """Ensure multiple arrays have the same length."""
    lengths = {len(a) for a in arrays}
    if len(lengths) != 1:
        raise ValueError("All arrays must have the same length")
