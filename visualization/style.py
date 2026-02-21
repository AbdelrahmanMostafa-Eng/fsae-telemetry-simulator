# style.py

"""
Global plotting style utilities for visualization modules.
Provides:
- Consistent color palette
- Default figure styling
- Helper function to apply global style settings

"""

from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class PlotStyleConfig:
    font_size: int = 12
    grid: bool = True
    facecolor: str = "white"
    palette: tuple = ("#1f77b4", "#ff7f0e", "#2ca02c",
                      "#d62728", "#9467bd", "#8c564b")


def apply_style(config: PlotStyleConfig = PlotStyleConfig()):
    """Apply global matplotlib style settings."""
    plt.rcParams.update({
        "figure.facecolor": config.facecolor,
        "axes.facecolor": config.facecolor,
        "axes.grid": config.grid,
        "font.size": config.font_size,
        "axes.prop_cycle": plt.cycler(color=config.palette)
    })


# Example usage and plotting

if __name__ == "__main__":
    apply_style()

    import numpy as np
    x = np.linspace(0, 10, 200)
    y = np.sin(x)

    plt.plot(x, y, label="sin(x)")
    plt.title("Styled Plot Example")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
