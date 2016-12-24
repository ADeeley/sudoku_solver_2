#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from sudoku.skeleton import fib

__author__ = "Adam Deeley"
__copyright__ = "Adam Deeley"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
