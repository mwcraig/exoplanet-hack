import numpy as np
import pytest

import etd


def test_midpoint():
    duration = 0.1  # days
    midpoint = 12.0  # days
    impact_param = 0.05
    assert (etd.z(midpoint, midpoint, duration, impact_param) ==
            impact_param)


def test_quarter_phase():
    duration = 0.1  # days
    midpoint = 12.0  # days
    impact_param = 0.05
    z_quarter = np.sqrt((1 + 3 * impact_param**2)/4)
    z = etd.z(midpoint - duration/4, midpoint, duration, impact_param)
    np.testing.assert_almost_equal(z, z_quarter)

    z = etd.z(midpoint + duration/4, midpoint, duration, impact_param)
    np.testing.assert_almost_equal(z, z_quarter)


def test_edpoints():
    duration = 0.1  # days
    midpoint = 12.0  # days
    impact_param = 0.05
    # At the endpoints of the eclipse z should be 1.
    z_end = etd.z(midpoint + duration/2, midpoint, duration, impact_param)
    z_begin = etd.z(midpoint - duration/2, midpoint, duration, impact_param)
    np.testing.assert_almost_equal(z_end, 1)
    np.testing.assert_almost_equal(z_begin, 1)
