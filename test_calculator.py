import calculator


class TestCalculator:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 24 == calculator.multiply(4, 6)

    def test_divide(self):
        assert 10 == calculator.divide(100, 10)
