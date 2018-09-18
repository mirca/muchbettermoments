# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = ["quadratic_2d"]

import numpy as np

def quadratic_2d(data):
    """
    Compute the quadratic estimate of the centroid in a 2d-array.

    Args:
        data (2darray): two dimensional data array

    Returns
        center (tuple): centroid estimate on the row and column directions,
                        respectively
    """
    arg_data_max = np.argmax(data)
    i, j = np.unravel_index(arg_data_max, data.shape)
    z_ = data[i-1:i+2, j-1:j+2]
    # our quadratic function is defined as
    # f(x, y | a, b, c, d, e, f) := a + b * x + c * y + d * x^2 + e * xy + f * y^2
    # therefore, the best fit coeffiecients are given as
    # note that they are unique and the uncertainty in each of them (#TODO) can be
    # computed following the derivations done by Vakili & Hogg (2016) and
    # Teague & Foreman-Mackey (2018)
    try:
        a = (-z_[0,0] + 2*z_[0,1] - z_[0,2] + 2*z_[1,0] + 5*z_[1,1] + 2*z_[1,2] -
             z_[2,0] + 2*z_[2,1] - z_[2,2]) / 9
        b = (-z_[0,0] - z_[0,1] - z_[0,2] + z_[2,0] + z_[2,1] + z_[2,2]) / 6
        c = (-z_[0,0] + z_[0,2] - z_[1,0] + z_[1,2] - z_[2,0] + z_[2,2]) / 6
        d = (z_[0,0] + z_[0,1] + z_[0,2] - z_[1,0]*2 - z_[1,1]*2 - z_[1,2]*2 +
             z_[2,0] + z_[2,1] + z_[2,2])/6
        e = (z_[0,0] - z_[0,2] - z_[2,0] + z_[2,2]) * .25
        f = (z_[0,0] - 2 * z_[0,1] + z_[0,2] + z_[1,0] - 2 * z_[1,1] + z_[1,2] +
             z_[2,0] - 2 * z_[2,1] + z_[2,2]) / 6
    except IndexError:
        return (i, j)

    # see https://en.wikipedia.org/wiki/Quadratic_function
    det = 4 * d * f - e ** 2
    xm = - (2 * f * b - c * e) / det
    ym = - (2 * d * c - b * e) / det
    return (i+xm, j+ym)
