#!/usr/bin/env python3

from typing import List

import itertools

if __name__ == '__main__':
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