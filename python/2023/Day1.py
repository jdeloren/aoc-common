import sys
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2023/day1.txt")


def tune(data):
    import re
    codex = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    total = 0
    for d in data:
        tuned = [c if c.isdigit() else codex[c] for c in re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', d)]
        total += int(tuned[0] + tuned[-1])
    return total

def calibrate(data):
    val = 0
    for d in data:
        ints = [i for i in d if i.isdigit()]
        val += int(ints[0] + ints[-1])
    return val

def second():
    print(f"(2023 2.0) calibration value => {tune(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four','4nineeightseven2', 'zoneight234', '7pqrstsixteen'])}")
    print(f"(2023 2.1) calibration value => {tune(input)}")

def first():
    print(f"(2023 1.0) calibration value => {calibrate(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7ychet'])}")
    print(f"(2023 1.1) calibration value => {calibrate(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
