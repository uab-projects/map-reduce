"""
Defines validators for the CLI arguments of this controller
"""


def positive_integer(arg):
    """
    Checks that the argument is a positive integer and if not, raises an
    exception. If it is, returns the argument as an integer

    Args:
        arg (str): string to check if can be converted to a positive integer

    Returns:
        int: converted string to integer

    Raises:
        ValueError: if string is not an integer or is less than 1
    """
    arg_int = int(arg)
    if arg_int <= 0:
        raise ValueError("Value %s is not a positive integer", arg)
    return arg_int


def positive_integer_or_zero(arg):
    """
    Checks that the argument is a positive integer or 0 and if not, raises an
    exception. If it is, returns the argument as an integer

    Args:
        arg (str): string to check if can be converted to a positive integer

    Returns:
        int: converted string to integer

    Raises:
        ValueError: if string is not an integer or is less than 0
    """
    arg_int = int(arg)
    if arg_int < 0:
        raise ValueError("Value %s is not a positive integer or 0", arg)
    return arg_int


def integer_greater_than_1(arg):
    """
    Checks that the argument is a positive integer greater than 1 and if not,
    raises an exception. If it is, returns the argument as an integer

    Args:
        arg (str): string to check if can be converted to a positive integer

    Returns:
        int: converted string to integer

    Raises:
        ValueError: if string is not an integer or is less than 2
    """
    arg_int = int(arg)
    if arg_int <= 1:
        raise ValueError("Value %s is not a positive integer greater than 1",
                         arg)
    return arg_int
