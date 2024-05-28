import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a = 4321
        b = 1234
        cal = Calculator()

        result = cal.subtract(a, b)

        expected = 3087
        assert result == expected

    def test_multiply(self):
        a = 5
        b = 5
        cal = Calculator()

        result = cal.multiply(a, b)

        expected = 25
        assert result == expected

    def test_divide(self):
        a = 5
        b = 5
        cal = Calculator()

        result = cal.divide(a, b)

        expected = 1
        assert result == expected

    def test_divide_by_zero(self):
        a = 4321
        b = 0
        cal = Calculator()

        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)