from typing import LiteralString
from operator import itemgetter

from python.day1.p1 import solve_lines
from python.constants import DAY_1_P2_STRING_INTS, DAY_1_INPUT_FILE


def string_ints_to_ints(my_str: LiteralString) -> LiteralString:
    """Convert integers in a string from word form to integer form and remove any non-int words.

    This implementation takes a sliding windows approach, successively passing over the string with
    an increasingly large window to filter out the integers. A regex approach would be faster, O(N)
    instead of O(n^2) but tbh I'm two glasses of wine deep and I don't feel like casting spells.

    >>> string_ints_to_ints("one")
    '1'

    >>> string_ints_to_ints("onetwo")
    '12'

    >>> string_ints_to_ints("one2three")
    '123'

    >>> string_ints_to_ints("hello")
    ''

    >>> string_ints_to_ints("hellothree")
    '3'

    >> string_ints_to_ints("sixteen")
    '6'

    Args:
        my_str (LiteralString): A string containing integers both in digit and
        written form (i.e. '7' and 'seven')
    """
    first_char_idx = 0
    end_char_idx = 1
    to_return: tuple[LiteralString, int] = []
    while (first_char_idx + end_char_idx) <= len(my_str):
        while (first_char_idx + end_char_idx) <= len(my_str):
            substring = my_str[first_char_idx : (first_char_idx + end_char_idx)]
            if substring in DAY_1_P2_STRING_INTS:
                to_return.append((DAY_1_P2_STRING_INTS[substring], first_char_idx))
            elif substring.isnumeric():
                to_return.append((substring, first_char_idx))
            first_char_idx += 1
        first_char_idx = 0
        end_char_idx += 1

    to_return = sorted(to_return, key=itemgetter(1))
    return "".join([item[0] for item in to_return])


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    with open(DAY_1_INPUT_FILE, "r") as f:
        print(
            solve_lines([string_ints_to_ints(line.strip()) for line in f.readlines()])
        )
