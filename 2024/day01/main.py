#!/usr/bin/env python

import typing


def part1() -> int:
    left: typing.List[int] = []
    right: typing.List[int] = []
    difference: typing.List[int] = []
    with open("input") as fp:
        for line in fp:
            content = line.split(" ")
            left.append(int(content[0]))
            right.append(int(content[-1]))
    left.sort()
    right.sort()
    pairs = zip(left, right)
    for n1, n2 in pairs:
        difference.append(abs(n1-n2))
    return sum(difference)


def part2() -> int:
    left: typing.List[int] = []
    right: typing.List[int] = []
    difference: typing.List[int] = []
    with open("input") as fp:
        for line in fp:
            content = line.split(" ")
            left.append(int(content[0]))
            right.append(int(content[-1]))
    left.sort()
    right.sort()
    for n1 in left:
        count = right.count(n1)
        if count >= 0:
            difference.append(n1*count)
    return sum(difference)


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
