from typing import LiteralString, Iterable
import python.constants as constants


def concat_first_last_int(char_int_string: LiteralString) -> LiteralString:
    """Return a string of the first and last integer in a string concatenated together.

    >>> concat_first_last_int("abc")
    ''

    >>> concat_first_last_int("1abc2")
    '12'

    >>> concat_first_last_int("1abc2def3")
    '13'

    >>> concat_first_last_int("abc1def")
    '11'

    Args:
        char_int_string (LiteralString): String of mixed characters and numbers.

    Returns:
        LiteralString: String of the first and last integer in the input string.
    """
    ints_in_string = [char for char in char_int_string if char.isnumeric()]
    if len(ints_in_string) == 0:
        return ""
    return ints_in_string[0] + ints_in_string[-1]


def int_str_to_int(line: LiteralString) -> int:
    """_summary_

    >>> int_str_to_int("")
    0

    >>> int_str_to_int("12")
    12

    Args:
        line (LiteralString): _description_

    Returns:
        int: _description_
    """
    if line == "":
        return 0
    else:
        return int(line)


def solve_lines(lines: Iterable[LiteralString]) -> int:
    """_summary_

    >>> solve_lines(["abc", "1abc2", "1abc2def3", "abc1def"])
    36

    Args:
        lines (Iterable[LiteralString]): _description_

    Returns:
        int: _description_
    """
    return sum((int_str_to_int(concat_first_last_int(line)) for line in lines))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    with open(constants.DAY_1_INPUT_FILE, "r") as f:
        print(solve_lines([line.strip() for line in f.readlines()]))
