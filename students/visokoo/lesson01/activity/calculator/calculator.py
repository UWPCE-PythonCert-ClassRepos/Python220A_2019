"""import custom exceptions class inheriting from exception"""
from .exceptions import InsufficientOperands


class Calculator(object):
    """
    Given two numbers, execute one of add, subtract, multiple & divide
    """

    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """
        Accepts a number argument and appends it to the class list: stack
        """
        self.stack.append(number)

    def _do_calc(self, operator):
        """
        Based on operator var, run respective module's calc method with
        values from class list stack.
        """
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """
        Call _do_calc method with adder module
        """
        return self._do_calc(self.adder)

    def subtract(self):
        """
        Call _do_calc method with subtracter module
        """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        Call _do_calc method with multiplier module
        """
        return self._do_calc(self.multiplier)

    def divide(self):
        """
        Call _do_calc method with divider module
        """
        return self._do_calc(self.divider)
