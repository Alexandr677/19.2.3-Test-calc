import pytest
from app.calculator import Calculator

class Testcalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 5) == 15

    def test_division_calculation_correctly(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_subtraction_calculation_correctly(self):
        assert self.calc.subtraction(self, 8, 4) == 4

    def test_adding_calculation_correctly(self):
        assert self.calc.adding(self, 8, 4) == 12