#!/usr/bin/env python3

from typing import List

import itertools


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


if __name__ == '__main__':
    increased: int = 0
    prev: int
    with open("input.txt", "r") as f:
        lines: List[int] = map(lambda x: int(str.strip(x)), f.readlines())

    for (first, second) in pairwise(lines):
        if second > first:
            increased += 1

    print(increased)