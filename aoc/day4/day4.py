from typing import List, Set, Tuple, Dict
from collections import defaultdict


def split_input_line(line: str) -> Tuple[str, List[str], List[str]]:
    """
    >>> line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    >>> split_input_line(line)
    ('Card 1', ['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53'])
    """
    card_num, rest = line.strip().split(":")
    win_nums, card_nums = rest.split("|")
    win_nums = win_nums.split()
    card_nums = card_nums.split()
    return card_num.strip(), win_nums, card_nums


def calculate_score_of(card_num: str, win_nums: List[str], my_nums: List[str]) -> int:
    """
    >>> line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    >>> card_num, win_nums, my_nums = split_input_line(line)
    >>> calculate_score_of(card_num, win_nums, my_nums)
    8
    """
    return int(2 ** (len([num for num in win_nums if num in my_nums]) - 1))  # floorit


def score_file(filepath: str) -> int:
    """
    >>> filepath = "inputs/day4/test.txt"
    >>> score_file(filepath)
    13
    """
    with open(filepath) as f:
        to_return = 0
        for line in f.readlines():
            card_num, win_nums, my_nums = split_input_line(line)
            to_return += calculate_score_of(card_num, win_nums, my_nums)
        return to_return


def score_cards(filepath):
    with open(filepath) as f:
        to_return = defaultdict(int)
        for line in f.readlines():
            card_num, win_nums, my_nums = split_input_line(line)
            to_return[int(card_num.split()[1])] = (
                calculate_score_of(card_num, win_nums, my_nums),
                len([num for num in win_nums if num in my_nums]),
            )
        return to_return


def count_cards(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

        card_counts = [1 for i in range(len(lines))]

        for line in lines:
            matches = 0
            # Count matching nums
            card, win_nums, card_nums = split_input_line(line)
            for num in win_nums:
                if num in card_nums:
                    matches += 1

            for copy in range(card_counts[lines.index(line)]):
                j = 1  # grab a copy of the card after our card“
                for i in range(matches):
                    card_counts[
                        lines.index(line) + j
                    ] += 1  # add a copy of the i + jth card
                    j += 1  # grab a copy of the next card
        return card_counts


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(score_file("inputs/day4/in.txt"))
    scored_cards = score_cards("inputs/day4/in.txt")
    counts = count_cards("inputs/day4/in.txt")
    print(sum(counts))
