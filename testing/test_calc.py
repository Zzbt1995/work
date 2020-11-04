import allure
import pytest
import yaml


# from pythoncode.caculator import Caculator

# 获取测试数据
def get_datas():
    with open('data/calc.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas


@allure.feature("计算器")
class TestCaculator:

    def setup_class(self):
        print("setup_class...")

    def teardown_class(self):
        print("teardown_class...")

    # def setup_method(self):
    #     self.calc = Caculator()
    #     print("【开始计算】")
    #
    # def teardown_method(self):
    #     print("【计算结束】")

    @pytest.mark.run(order=1)
    @allure.story("加法")
    # @pytest.mark.parametrize('a,b,expect', [(1, 2, 3), (1, 1.4, 2.4), (8.8, 0.2, 9), (20, -12, 8),
    #                                         (9223372036854775807, 1, 9223372036854775808), (1, 1, 3)],
    #                          ids=['int+int', 'int+float', 'float+float', 'integer+iegative', 'BigNumber', 'make a failure'])
    @pytest.mark.parametrize("a,b,expect", get_datas()['add']['datas'], ids=get_datas()['add']['ids'])
    def test_add(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=3)
    @allure.story("减法")
    @pytest.mark.parametrize("a,b,expect", get_datas()['sub']['datas'], ids=get_datas()['sub']['ids'])
    def test_sub(self, get_calc, a, b, expect):
        # result = self.calc.sub(a, b)
        result = round(get_calc.sub(a, b), 10)
        assert result == expect

    @pytest.mark.run(order=4)
    @allure.story("乘法")
    # @pytest.mark.parametrize('a,b,expect', [(0, 2, 0), (2, -4, -8), (10, 0.2, 2)])
    @pytest.mark.parametrize("a,b,expect", get_datas()['mul']['datas'], ids=get_datas()['mul']['ids'])
    def test_mul(self, get_calc, a, b, expect):
        # result = self.calc.mul(a, b)
        result = round(get_calc.mul(a, b), 10)
        assert result == expect

    @pytest.mark.run(order=2)
    @allure.story("除法")
    # @pytest.mark.parametrize('a,b,expect',
    #                          [(1, 2, 0.5), (2, 0.5, 4), (8.8, 8.8, 1), (20, -2, -10), (1, 0, ZeroDivisionError)],
    #                          ids=['int/int', 'int/float', 'float/float', 'integer/iegative', 'Zero Division'])
    @pytest.mark.parametrize("a,b,expect", get_datas()['div']['datas'], ids=get_datas()['div']['ids'])
    def test_div(self, get_calc, a, b, expect):
        if b != 0:
            # result = self.calc.div(a, b)
            result = get_calc.div(a, b)
            assert result == expect
        if b == 0:
            try:
                get_calc.div(a, b)
            except ZeroDivisionError as e:
                print("Divesion by Zero")
