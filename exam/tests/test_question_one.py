"""Confirm the correctness of functions in question_one."""

import pytest

# ruff: noqa: PLR2004
from questions.question_one import (
    find_average_value,
    find_maximum_value,
    find_minimum_value,
)


@pytest.mark.question_one_part_a
def test_find_minimum_value():
    """Confirm correctness of question part."""
    # check 1: Matrix with positive values
    matrix = [[5, 7, 3], [1, 9, 2], [6, 4, 8]]
    minimum_positive = find_minimum_value(matrix)
    assert (
        1 == minimum_positive and minimum_positive is not None
    ), "Minimum positive value in matrix"
    # check 2: Matrix with negative values
    matrix = [[-2, 5, 1], [-3, 0, 6], [-1, -4, 7]]
    minimum_negative = find_minimum_value(matrix)
    assert (
        -4 == minimum_negative and minimum_negative is not None
        # )
    ), "Minimum negative value in matrix"
    # check 3: Matrix with a single element
    matrix = [[10]]
    minimum_single = find_minimum_value(matrix)
    assert (
        10 == minimum_single and minimum_single is not None
    ), "Minimum value in single matrix"
    # check 4: Empty matrix
    matrix = []
    minimum_empty = find_minimum_value(matrix)
    assert minimum_empty is None, "Minimum value in empty matrix"


@pytest.mark.question_one_part_b
def test_find_maximum_value():
    """Confirm correctness of question part."""
    # check 1: Matrix with positive values
    matrix = [[5, 7, 3], [1, 9, 2], [6, 4, 8]]
    maximum_positive = find_maximum_value(matrix)
    assert 9 == maximum_positive, "Maximum positive value in matrix"
    # check 2: Matrix with negative values
    matrix = [[-2, 5, 1], [-3, 0, 6], [-1, -4, 7]]
    maximum_negative = find_maximum_value(matrix)
    assert 7 == maximum_negative, "Maximum negative value in matrix"
    # check 3: Matrix with a single element
    matrix = [[10]]
    maximum_single = find_maximum_value(matrix)
    assert 10 == maximum_single, "Maximum value in single matrix"
    # check 4: Empty matrix
    matrix = []
    maximum_empty = find_maximum_value(matrix)
    assert maximum_empty is None, "Maximum value in empty matrix"


@pytest.mark.question_one_part_c
def test_find_average_value():
    """Confirm correctness of a question part."""
    # check 1: Matrix with positive values
    matrix = [[5, 7, 3], [1, 9, 2], [6, 4, 8]]
    average_positive = find_average_value(matrix)
    assert 5.0 == average_positive, "Average value in matrix with positive numbers"
    # check 2: Matrix with negative values
    matrix = [[-2, 5, 1], [-3, 0, 6], [-1, -4, 7]]
    average_negative = find_average_value(matrix)
    assert 1.0 == average_negative, "Average value in matrix with negative numbers"
    # check 3: Matrix with a single element
    matrix = [[10]]
    average_single = find_average_value(matrix)
    assert 10.0 == average_single, "Average value in single element matrix"
    # check 4: Empty matrix
    matrix = []
    average_empty = find_average_value(matrix)
    assert average_empty is None, "Average value in empty matrix"