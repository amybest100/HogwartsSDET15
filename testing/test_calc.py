import pytest

from pythoncode.calculator import Calculator


def test_a():
    print("test case a")


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2]
    ], ids=['int_case', 'bignum_case', 'float_case'])
    def test_add(self, a, b, expect):
        # calc=Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('c,d,expect1', [
        [20, 3, 17], [50, 20, 30], [0.9, 0.1, 0.8]
    ])
    def test_sub(self, c, d, expect1):
        # calc=Calculator()
        result = self.calc.sub(c, d)
        assert result == expect1

    @pytest.mark.parametrize('e,f,expect2', [
        [2, 3, 6], [4, 6, 24], [5, 7, 35], [8, 0, 0]
    ])
    def test_mul(self, e, f, expect2):
        # calc=Calculator()
        result = self.calc.mul(e, f)
        assert result == expect2

    @pytest.mark.parametrize('g,h,expect3', [
        [9, 1, 9], [77, 11, 7], [8, 0, 2]
    ])
    def test_div(self, g, h, expect3):
        # calc=Calculator()
        result = self.calc.div(g, h)
        assert result == expect3
