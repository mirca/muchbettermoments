# -*- coding: utf-8 -*-

from __future__ import division, print_function

import pytest
import numpy as np

from muchbettermoments import quadratic_2d

def test_recover_center_no_noise():
    u = np.linspace(0, 8, 9)
    x, y = np.meshgrid(u, u)
    true_center = [3.45, 4.73]

    z = 100 - (x - true_center[1]) ** 2 - (y - true_center[0]) ** 2
    coeffs, center = quadratic_2d(z)
