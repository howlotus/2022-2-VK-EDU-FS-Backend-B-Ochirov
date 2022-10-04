"""This module implements function to check input string"""


def is_number(input_str) -> bool:
    """This function checks if input string is convertable to integer"""

    try:
        int(input_str)
        return True
    except ValueError:
        return False
