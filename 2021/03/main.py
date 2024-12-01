#!/usr/bin/env python3


def part1():
    """
    Read the bit per line, instead of reading everything and computing
    the gamma and epsilon rates.
    """
    with open("input.txt", "r") as f:
        inst = map(str.strip, f.readlines())
    inst = list(inst)

    gamma: str = ''
    epsilon: str = ''
    for j in range(len(inst[0])):
        num0 = 0
        num1 = 0
        for i in range(len(inst)):
            if int(inst[i][j]) == 1:
                num1 += 1
            else:
                num0 += 1
        if num0 > num1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print(int(gamma, 2)*int(epsilon, 2))


def part2():
    pass


if __name__ == '__main__':
    part1()
