"""
Calculator Module
"""
from .exceptions import InsufficientOperands


class Calculator:
    """
    Performs calculation calling appropriate module
    """

    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """
        Gets numbers to use in calculator
        :param number:
        :return:
        """
        # Insert method is adding to the beginning of stack list at index 0
        # self.stack.insert(0, number)

        # Append method adds to end of stack list
        self.stack.append(number)

    def _do_calc(self, operator):
        """
        Calculate
        :param operator:
        :return:
        """
        # result = operator.calc(self.stack[0], self.stack[1])

        # if less than 2 operators are entered raise exception
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """
        Add
        :return:
        """
        return self._do_calc(self.adder)

    def subtract(self):
        """
        Subtract
        :return:
        """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        Multiply
        :return:
        """
        return self._do_calc(self.multiplier)

    def divide(self):
        """
        Divide
        :return:
        """
        return self._do_calc(self.divider)
