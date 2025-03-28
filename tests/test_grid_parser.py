import pytest

from src.main import (
    find_greatest_product_of_contiguous_integers,
    is_direction_possible,
    calculate_product_of_continuous_integers,
)

# Test is the direction is possible (5x5 dummy grid)
def test_is_direction_possible():
    grid = [[1] * 5 for _ in range(5)]
    k = 3

    # Right
    assert is_direction_possible(0, 0, 5, 5, "right", k) is True
    assert is_direction_possible(0, 3, 5, 5, "right", k) is False

    # Down
    assert is_direction_possible(0, 0, 5, 5, "down", k) is True
    assert is_direction_possible(3, 0, 5, 5, "down", k) is False

    # Down-right
    assert is_direction_possible(0, 0, 5, 5, "down_right", k) is True
    assert is_direction_possible(3, 3, 5, 5, "down_right", k) is False

    # Up-right
    assert is_direction_possible(2, 0, 5, 5, "up_right", k) is True
    assert is_direction_possible(0, 3, 5, 5, "up_right", k) is False


def test_calculate_product_of_continuous_integers():
    grid = [[1] * 5 for _ in range(5)]
    k = 3

    # All values are 1, so product should be 1
    assert calculate_product_of_continuous_integers(grid, 0, 0, "right", k) == 1
    assert calculate_product_of_continuous_integers(grid, 0, 0, "down", k) == 1
    assert calculate_product_of_continuous_integers(grid, 0, 0, "down_right", k) == 1
    assert calculate_product_of_continuous_integers(grid, 2, 0, "up_right", k) == 1


def test_find_greatest_product_of_continuous_integers():
    grid = [[1] * 5 for _ in range(5)]
    max_product = find_greatest_product_of_contiguous_integers(grid, 3)

    # All values are 1s, so product = 1
    assert max_product == 1


def test_known_product_in_sample_grid():
    grid = [
        [8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],  # 4, 60, 11 = 2640
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45],
    ]
    result = find_greatest_product_of_contiguous_integers(grid, 3)
    assert result >= 2640
