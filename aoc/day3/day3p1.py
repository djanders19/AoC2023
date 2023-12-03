from typing import List, Any
from collections import defaultdict


def file_to_2d_grid(filepath: str) -> List[List[str]]:
    """Convert a grid .txt file to a Grid datastructure.

    >>> filepath = "inputs/day3/day3_test.txt"
    >>> file_to_2d_grid(filepath)[0:2]
    [["467..114..], ["...*......"]]

    Args:
        filepath (str): _description_

    Returns:
        List[List[str]]: _description_
    """
    with open(filepath) as f:
        return [line.strip() for line in f.readlines()]


def xy_coord_in_bounds(x: int, y: int, grid: List[List[Any]]) -> bool:
    """Check if an XY coordinate is in bounds of a given grid. Negative indices
    return false.

    >>> l = [[]]
    >>> xy_coord_in_bounds(1, 2, l)
    False

    >>> l = [[1,2],[3,4]]
    >>> xy_coord_in_bounds(0,0,l)
    True
    >>> xy_coord_in_bound(1,1,l)
    False
    >>> xy_coord_in_bounds(-1,0,l)
    False
    >>> xy_coord_in_bounds(2, 0, l)
    False

    Args:
        x (int): _description_
        y (int): _description_
        grid (List[List[int]]): _description_

    Returns:
        bool: True if in bounds, else False.
    """
    if x < 0 or y < 0:
        return False
    try:
        grid[x][y]
        return True
    except IndexError:
        return False


def is_symbol(char: str) -> bool:
    """Check if a value is a symol.

    Symbols are defined as non-numeric characters not equal to '.'.

    >>> is_symbol(".")
    False

    >>> is_symbol("3")
    False

    >>> is_symbol("$")
    True

    >>> is_symbol("A")
    return True

    Args:
        char (str): char to check

    Returns:
        bool: True if given char is a symbol, else False.
    """
    not_a_symbol = set(".")
    if char in not_a_symbol or char.isdigit():
        return False
    return True


def check_adjacencies_for_symbol(x, y, grid):
    xx = x - 1

    while xx <= x + 1:
        yy = y - 1
        while yy <= y + 1:
            if xy_coord_in_bounds(xx, yy, grid):
                char = grid[xx][yy]
                if is_symbol(char):
                    return True
            yy += 1
        xx += 1
    return False


def is_part_number(x, y, grid):
    # Base cases:
    if not xy_coord_in_bounds(x, y, grid):
        return False  # End of word
    if grid[x][y] == ".":
        return False  # End of word

    return check_adjacencies_for_symbol(x, y, grid) or is_part_number(x, y + 1, grid)


def extract_part_nums(grid: List[List[str]]):
    x = 0
    part_nums: List[int] = []
    part_num_map = defaultdict(list)

    while x < len(grid):
        y = 0
        while y < len(grid[0]):
            if grid[x][y].isdigit() and is_part_number(x, y, grid):
                part_num = ""
                part_num_idx_one = y
                while y < len(grid[0]) and grid[x][y].isdigit():
                    part_num += grid[x][y]
                    y += 1  # Advance to end of number
                part_nums.append(int(part_num))
                part_num_idx_two = y
                part_num_map[x].append((part_num_idx_one, part_num_idx_two))
            y += 1
        x += 1
    return part_nums, part_num_map


def get_part_nums_next_to_coord(x, y, part_num_map, grid):
    part_nums = []
    x_start = x - 1
    x_end = x + 2
    if x == 0:
        x_start = 0
    if x_end > len(grid):
        x_end = x + 1

    for xx in range(x_start, x_end):
        for part_num_y_coords in part_num_map[xx]:
            if y in range(part_num_y_coords[0] - 1, part_num_y_coords[1] + 1):
                part_nums.append(grid[xx][part_num_y_coords[0] : part_num_y_coords[1]])
    return [int(part_num) for part_num in part_nums]


def get_gear_ratios(grid, part_num_map):
    gear_ratios = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "*":
                adjacent_part_nums = get_part_nums_next_to_coord(
                    x, y, part_num_map, grid
                )
                if len(adjacent_part_nums) == 2:
                    gear_ratios.append(adjacent_part_nums[0] * adjacent_part_nums[1])
    return gear_ratios


def main():
    grid = file_to_2d_grid("inputs/day3/day3_in.txt")
    part_nums, part_num_map = extract_part_nums(grid)
    print(sum(part_nums))

    print(sum(get_gear_ratios(grid, part_num_map)))


if __name__ == "__main__":
    main()
