#!/usr/bin/env python3

from typing import List

import itertools
import math


def part1():
    horizontal: int = 0
    vertical: int = 0

    with open("input.txt", "r") as f:
        lines: List[str] = map(str.strip, f.readlines())

    for line in lines:
        if line.startswith("forward"):
            _, places = line.split(" ")
            horizontal += int(places)
        elif line.startswith("down"):
            _, places = line.split(" ")
            vertical += int(places)
        elif line.startswith("up"):
            _, places = line.split(" ")
            vertical -= int(places)

    print(horizontal, vertical)
    print(horizontal * vertical)


def part2():
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    with open("input.txt", "r") as f:
        lines: List[str] = map(str.strip, f.readlines())

    for line in lines:
        if line.startswith("forward"):
            # forward X does two things:

            # It increases your horizontal position by X units.
            # It increases your depth by your aim multiplied by X.
            _, places = line.split(" ")
            horizontal += int(places)
            depth += aim * int(places)
        elif line.startswith("down"):
            _, places = line.split(" ")
            aim += int(places)
        elif line.startswith("up"):
            _, places = line.split(" ")
            aim -= int(places)
    print(horizontal * depth)


if __name__ == '__main__':
    part2()
