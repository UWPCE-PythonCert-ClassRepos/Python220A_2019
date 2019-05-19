# -------------------------------------------------------------------------------------------------------------------- #
# Title: Test Calculator Integration
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-04-09, Initial release
# -------------------------------------------------------------------------------------------------------------------- #

from unittest import TestCase

from calculator.adder import Adder
from calculator.subtracter import Subtracter
from calculator.multiplier import Multiplier
from calculator.divider import Divider
from calculator.calculator import Calculator


class ModuleTest(TestCase):

    def test_module(self):
        calculator = Calculator(Adder(), Subtracter(), Multiplier(), Divider())

        calculator.enter_number(5)
        calculator.enter_number(2)
        calculator.multiply()
        calculator.enter_number(46)
        calculator.add()
        calculator.enter_number(8)
        calculator.divide()
        calculator.enter_number(1)
        result = calculator.subtract()

        self.assertEqual(6, result)

