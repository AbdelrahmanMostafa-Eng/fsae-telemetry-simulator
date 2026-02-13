#plotting.py

"""

Generic plotting helpers used across the FSAE Telemetry Simulator.
These functions keep visualizations consistent and clean.

"""

import matplotlib.pyplot as plt


def setup_plot(title: str, xlabel: str, ylabel: str):
    """Apply consistent styling to all plots."""
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)


def show():
    """Wrapper for plt.show() to keep imports clean."""
    plt.show()
