import Lab2 as temperature
import statistics
import pytest

def test_calc_average_temperature():
    numbers = [20, 25, 30, 35, 40]
    expected_result = sum(numbers) / len(numbers)
    assert temperature.calc_average_temperature(numbers) == expected_result

def test_calc_min_max_temperature():
    numbers = [20, 25, 30, 35, 40]
    expected_min = min(numbers)
    expected_max = max(numbers)
    expected_list = sorted(numbers)
    assert temperature.calc_min_max_temperature(numbers) == (expected_min, expected_max, expected_list)

def test_calc_median_temperature():
    numbers = [20, 25, 30, 35, 40]
    expected_median = statistics.median(numbers)
    assert temperature.calc_median_temperature(numbers) == expected_median