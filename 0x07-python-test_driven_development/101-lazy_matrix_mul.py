#!/usr/bin/python3
"""
101-lazy_matrix_mul.py
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    m_a and m_b must be an list of lists of integers or floats
    """
    return (np.matmul(m_a, m_b))
