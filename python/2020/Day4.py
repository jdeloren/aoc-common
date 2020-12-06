import sys
from common import DataAnalyzer


required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional = ['cid']


def passports(data):
    valid = 0
    passports = []
    current = required.copy()

    for str in data:
        if not str:
            current = required.copy()
            continue

        fields = str.split()
        for field in fields:
            key = field.split(':')[0]
            current.remove(key) if key in current

        if not current:
            valid += 1

    return valid


def second():
    pass


def first():
    data = DataAnalyzer.load("2020/day4.txt")
    print("(4.1) valid passports {:d}".format(passports(data)))


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()


if __name__ == '__main__':
    solve(sys.argv[1])
