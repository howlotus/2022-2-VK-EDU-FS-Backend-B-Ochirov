class CustomError(Exception):
    """Base exception for custom errors"""


class NotNumberError(CustomError):
    """This exception raises, when user enters not a number"""


class OccupiedCellError(CustomError):
    """This exception raises, when user tries to enter an occupied cell"""


class OutOfRangeError(CustomError):
    """This exception raises, when user enters a number out of range from 1 to 9"""
