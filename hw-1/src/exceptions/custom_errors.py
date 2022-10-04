"""This module implements custom errors"""


class InvalidArgsError(Exception):
    """This exception raises, when user enters many arguments"""


class NotNumberError(Exception):
    """This exception raises, when user enters not a number"""


class OccupiedCellError(Exception):
    """This exception raises, when user tries to enter an occupied cell"""


class OutOfRangeError(Exception):
    """This exception raises, when user enters a number out of range from 1 to 9"""
