from dataclasses import dataclass, field
from typing import Dict, LiteralString, List
from collections import defaultdict
from enum import Enum
import re

from python.constants import DAY_2_INPUT_FILE, DAY_2_TEST_FILE


class CubeColor(Enum):
    BLUE = 1
    RED = 2
    GREEN = 3
    UNKOWN = 4

    @classmethod
    def from_string(cls, color_str: LiteralString):
        match color_str:
            case "blue":
                return cls(CubeColor.BLUE)
            case "red":
                return cls(CubeColor.RED)
            case "green":
                return cls(CubeColor.GREEN)
            case _:
                return cls(CubeColor.UNKOWN)


@dataclass
class Round:
    color_counts: Dict[CubeColor, int] = field(default_factory=defaultdict)

    @classmethod
    def from_string(cls, round_string: str):
        split_strings = [s.strip(" ;") for s in round_string.split(",")]
        counts = defaultdict(int)
        for string in split_strings:
            match string.split():
                case count, color:
                    counts[CubeColor.from_string(color)] = int(count)
                case _:
                    raise Exception("Malformed Round-String: ", string)
        return cls(counts)

    def possible(self, arrangement: Dict[CubeColor, int]) -> bool:
        for color, count in arrangement.items():
            if self.color_counts[color] > count:
                return False
        return True

    def min_arrangement(self) -> Dict[CubeColor, int]:
        return self.color_counts


@dataclass
class Game:
    game_num: int
    rounds: List[Round]

    @classmethod
    def from_string(cls, game_string):
        pattern = r"Game (\d+): (.*)"
        match = re.match(pattern, game_string)

        if match:
            game_number, rounds = match.groups()
            rounds_list = [Round.from_string(s) for s in rounds.split(";")]
            return cls(int(game_number), rounds_list)
        else:
            raise Exception("Invalid game string!")

    def possible(self, arrangement: Dict[CubeColor, int]) -> bool:
        possible_rounds = [round.possible(arrangement) for round in self.rounds]
        return all(possible_rounds)  # Only possible if all rounds are possible

    def min_arrangement(self) -> Dict[CubeColor, int]:
        to_return = defaultdict(int)
        for round in self.rounds:
            min_arrangement_for_round = round.min_arrangement()
            for key, value in min_arrangement_for_round.items():
                if value > to_return[key]:
                    to_return[key] = value
        return to_return


def power(arrangement: Dict[CubeColor, int]):
    product = 1
    for value in arrangement.values():
        product *= value
    return product


if __name__ == "__main__":
    round = "3 blue, 4 red; "
    round = Round.from_string(round)
    print(round)

    game = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"
    print(Game.from_string(game))

    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    arrangement = {CubeColor.RED: 12, CubeColor.GREEN: 13, CubeColor.BLUE: 14}

    with open(DAY_2_TEST_FILE) as f:
        games = [Game.from_string(line.strip()) for line in f.readlines()]
        possible_game_nums = [
            game.game_num for game in games if game.possible(arrangement)
        ]
        summed_game_nums = sum(possible_game_nums)
        print(f"Summed game nums test: {summed_game_nums}")

        print(
            f"Summed power test: {sum([power(game.min_arrangement()) for game in games])}"
        )

    with open(DAY_2_INPUT_FILE) as f:
        games = [Game.from_string(line.strip()) for line in f.readlines()]
        possible_game_nums = [
            game.game_num for game in games if game.possible(arrangement)
        ]
        summed_game_nums = sum(possible_game_nums)
        print(f"Summed game nums: {summed_game_nums}")

        print(f"Summed power: {sum([power(game.min_arrangement()) for game in games])}")
