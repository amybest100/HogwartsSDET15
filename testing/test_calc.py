import pytest

from pythoncode.calculator import Calculator


def test_a():
    print("test case a")


class TestCalc:
    def setup_class(self):
        print("计算器开始工作")

    def teardown_class(self):
        print("计算器结束工作")

    def setup(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown(self):
        print("计算结束")

    # 加法，整数、小数、负数
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [0.3, 0.2, 0.5], [-3, -6, -9]
    ])
    def test_add(self, a, b, expect):
        # calc=Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    #减法，整数、小数、负数
    @pytest.mark.parametrize('c,d,expect1', [
        [20, 3, 17], [1.8, 0.5, 1.3], [-7, 1, -8]
    ])
    def test_sub(self, c, d, expect1):
        # calc=Calculator()
        result = self.calc.sub(c, d)
        assert result == expect1

    # 乘法，整数、小数、负数、与0相乘
    @pytest.mark.parametrize('e,f,expect2', [
        [2, 3, 6], [0.8, 0.6, 0.48], [-7, -9, 63], [8, 0, 0]
    ])
    def test_mul(self, e, f, expect2):
        # calc=Calculator()
        result = self.calc.mul(e, f)
        assert result == expect2

    # 除法，整数、小数、负数、除数为0，被除数为0
    @pytest.mark.parametrize('g,h,expect3', [
        [9, 1, 9], [2, 0.5, 4], [-10, 2, -5], [8, 0, "You can't divide by zero!"], [0, 6, 0]
    ])
    def test_div(self, g, h, expect3):
        # calc=Calculator()
        result = self.calc.div(g, h)
        assert result == expect3
