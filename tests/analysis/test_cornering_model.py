# test_cornering_model.py

import numpy as np
from cornering_model import CorneringModel


def test_cornering_speed_increases_with_radius():
    model = CorneringModel(mass=230, mu=1.8, downforce_coeff=10)

    v_small = model.cornering_speed(20)
    v_large = model.cornering_speed(100)

    assert v_large > v_small


def test_cornering_speed_positive():
    model = CorneringModel(mass=230, mu=1.8, downforce_coeff=10)
    v = model.cornering_speed(50)

    assert v > 0
