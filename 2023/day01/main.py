import re
import typing


def part1() -> int:
    numbers: typing.List[int] = []
    with open("input") as fp:
        for line in fp:
            matches = re.findall(r"[0-9]", line)
            numbers.append(int(matches[0]+matches[-1]))
    return sum(numbers)


def part2():
    def inline(string: typing.AnyStr, replacements: typing.Dict[str, str]):
        for key, value in replacements.items():
            string = string.replace(key, value)
        return string
    replace: typing.Dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    weird: typing.Dict[str, str] = {
        "oneight": "oneeight",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "nineight": "nineeight",
        "twone": "twoone",
        "sevenine": "sevennine",
        "eightwo": "eighttwo",
    }
    numbers: typing.List[int] = []
    with open("input") as fp:
        for line in fp:
            matches = re.findall("([0-9])", inline(inline(line.strip(), replacements=weird), replacements=replace))
            numbers.append(int(matches[0])*10 + int(matches[-1]))
    return sum(numbers)


if __name__ == '__main__':
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")
