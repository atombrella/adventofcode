#!/usr/bin/env python

from typing import Any, List


# https://jamescooper.substack.com/p/using-python-classes-to-create-bingo

class Board:

    def __init__(self, rows: List[int]) -> None:
        self.rows = rows

    def is_bingo(self) -> bool:
        return False


def main(args: Any):
    pass


if __name__ == '__main__':

    with open("input.txt", "r") as file:
        lines = file.readlines()

    # play the bingo by

    # get the 
