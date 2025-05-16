import pytest
from my_awesome_lib.math_tools import calculate_mean, solve_quadratic

def test_calculate_mean_normal():
    assert calculate_mean([2, 4, 6]) == 4

def test_calculate_mean_empty():
    with pytest.raises(ValueError):
        calculate_mean([])

def test_solve_quadratic_two_roots():
    result = solve_quadratic(1, -3, 2)
    assert set(result) == {1.0, 2.0}

def test_solve_quadratic_one_root():
    result = solve_quadratic(1, -2, 1)
    assert result == (1.0,)

def test_solve_quadratic_no_root():
    assert solve_quadratic(1, 0, 1) == ()
