from aoc.day1 import p1 as day1_p1, p2 as day1_p2
from aoc.day2 import day2p1
from aoc.day3 import day3p1


def run_all():
    # Execute main functions from each day/problem
    print("\nDAY 1:")
    day1_p1.main()
    day1_p2.main()

    print("\nDAY 2:")
    day2p1.main()

    print("\nDAY 3:")
    day3p1.main()


if __name__ == "__main__":
    run_all()
