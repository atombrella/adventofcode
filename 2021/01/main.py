#!/usr/bin/env python3

from typing import List, Tuple

import itertools


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def part1():
    increased: int = 0
    prev: int
    with open("input.txt", "r") as f:
        lines: List[int] = map(lambda x: int(str.strip(x)), f.readlines())

    for (first, second) in pairwise(lines):
        if second > first:
            increased += 1

    print(increased)


def part2():
    increased: int = 0
    prev: int
    with open("input.txt", "r") as f:
        lines: List[int] = map(lambda x: int(str.strip(x)), f.readlines())

    triplets: List[Tuple[int, int, int]] = list(triplewise(lines))
    prev = sum(triplets[0])
    print(prev)

    for s in triplets[1:]:
        if sum(s) > prev:
            increased += 1
        prev = sum(s)

    print(increased)


if __name__ == '__main__':
    part2()
