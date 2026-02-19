# plotting.py

"""
General plotting utilities for analysis modules.
Provides:
- Line plot helper
- Scatter plot helper
- Consistent styling for analysis visualizations

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class PlotStyle:
    title: str = ""
    xlabel: str = ""
    ylabel: str = ""
    grid: bool = True
    legend: bool = True


class Plotting:
    @staticmethod
    def line(x: np.ndarray, y: np.ndarray, label: str = None, style: PlotStyle = None):
        """Create a simple line plot."""
        plt.plot(x, y, label=label)
        if style:
            Plotting._apply_style(style)

    @staticmethod
    def scatter(x: np.ndarray, y: np.ndarray, label: str = None, style: PlotStyle = None):
        """Create a simple scatter plot."""
        plt.scatter(x, y, label=label)
        if style:
            Plotting._apply_style(style)

    @staticmethod
    def _apply_style(style: PlotStyle):
        """Apply consistent styling to plots."""
        if style.title:
            plt.title(style.title)
        if style.xlabel:
            plt.xlabel(style.xlabel)
        if style.ylabel:
            plt.ylabel(style.ylabel)
        if style.grid:
            plt.grid(True)
        if style.legend:
            plt.legend()


# Example usage

if __name__ == "__main__":
    x = np.linspace(0, 10, 200)
    y = np.sin(x)

    style = PlotStyle(
        title="Sine Wave Example",
        xlabel="Time (s)",
        ylabel="Amplitude",
        grid=True,
        legend=True
    )

    Plotting.line(x, y, label="sin(x)", style=style)
    plt.show()
