# test_style.py

import matplotlib
matplotlib.use("Agg")

from style import apply_style, PlotStyleConfig


def test_apply_style_runs():
    config = PlotStyleConfig(font_size=10)
    apply_style(config)
