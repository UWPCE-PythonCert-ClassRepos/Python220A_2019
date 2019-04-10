"""Python 201 Lesson 01 Calculator"""
from .exceptions import InsufficientOperands


class Calculator():
    """ Calculator Class """

    def __init__(self, adder, subtracter, multiplier, divider):
        """ init method """

        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """ enter_number method """

        self.stack.insert(0, number)

    def _do_calc(self, operator):
        """ do_calc """

        try:
            result = operator.calc(self.stack[1], self.stack[0])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """ add method """

        return self._do_calc(self.adder)

    def subtract(self):
        """ subtract method """

        return self._do_calc(self.subtracter)

    def multiply(self):
        """ multiply method """

        return self._do_calc(self.multiplier)

    def divide(self):
        """ divide """

        return self._do_calc(self.divider)
