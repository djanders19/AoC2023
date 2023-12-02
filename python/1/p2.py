from python.constants import DAY_1_P2_STRING_INTS


def string_ints_to_ints(my_str: str) -> str:
    """_summary_

    >>> string_ints_to_ints("one")
    '1'

    >>> string_ints_to_ints("onetwo")
    '12'

    >>> string_ints_to_ints("one2three")
    '123'

    >>> string_ints_to_ints("hello")
    'hello'

    >>> string_ints_to_ints("hellothree")
    'hello3'

    >> string_ints_to_ints("sixteen")
    '6'

    Args:
        my_str (LiteralString): A string containing integers both in digit and
        written form (i.e. '7' and 'seven')
    """
    i = 0
    j = 1
    to_return = ""
    while (j - i) < len(my_str):
        while (i + j) < len(my_str):
            substring = my_str[i:j]
            if substring in DAY_1_P2_STRING_INTS:
                to_return = to_return + DAY_1_P2_STRING_INTS[substring]
    return to_return


if __name__ == "__main__":
    import doctest

    doctest.testmod()
