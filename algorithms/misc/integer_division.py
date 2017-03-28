def integer_division_recursive(x, y):
    """
    Give the result of x / y (integer division, discarding remainder) without using the / or * operators
    """
    if y == 0:
        raise ZeroDivisionError
    if x < 0 and y < 0:
        return integer_division_recursive_helper(0 - x, 0 - y, 0)
    if x < 0:
        times_y_in_positive_x = integer_division_recursive_helper(0 - x, y, 0)
        return 0 - times_y_in_positive_x
    if y < 0:
        times_positive_y_in_x = integer_division_recursive_helper(x, 0 - y, 0)
        return 0 - times_positive_y_in_x
    else:
        return integer_division_recursive_helper(x, y, 0)


def integer_division_recursive_helper(x, y, i):
    if x == 0:
        return i
    if x < 0:
        return i - 1
    else:
        return integer_division_recursive_helper(x - y, y, i + 1)


def integer_division_iterative(x, y):
    if y == 0:
        raise ZeroDivisionError
    if x < 0 and y < 0:
        return integer_division_iterative_helper(0 - x, 0 - y)
    if x < 0:
        times_y_in_positive_x = integer_division_iterative_helper(0 - x, y)
        return 0 - times_y_in_positive_x
    if y < 0:
        times_positive_y_in_x = integer_division_iterative_helper(x, 0 - y)
        return 0 - times_positive_y_in_x
    else:
        return integer_division_iterative_helper(x, y)


def integer_division_iterative_helper(x, y):
    decumulator = x
    i = 0
    while True:
        if decumulator == 0:
            return i
        if decumulator < 0:
            return i - 1
        else:
            decumulator -= y
            i += 1