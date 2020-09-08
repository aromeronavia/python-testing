import pytest


class Calculator:
    def sum(self, a, b):
        return a + b


class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.calculator = Calculator()

    def test_sum_operation(self):
        assert self.calculator.sum(1, 2) == 3

    def test_diff_operation(self):
        assert self.calculator.sum(1, 2) == 3
