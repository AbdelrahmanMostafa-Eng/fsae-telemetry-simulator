# test_aero_map.py

import numpy as np
from aero_map import AeroMap


def test_drag_increases_with_speed():
    aero = AeroMap(cd=1.0, cl=2.0, area=1.5)

    d1 = aero.drag_force(10)
    d2 = aero.drag_force(30)

    assert d2 > d1


def test_downforce_positive():
    aero = AeroMap(cd=1.0, cl=3.0, area=1.5)
    df = aero.downforce(50)

    assert df > 0
