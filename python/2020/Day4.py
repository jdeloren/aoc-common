import sys
from common import DataAnalyzer


required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional = ['cid']

def range_check(value, min, max):
    return value >= min and value <= max


def audit_birthdate(value):
    return len(value) == 4 and range_check(int(value), 1920, 2002)


def audit_issuedate(value):
    return len(value) == 4 and range_check(int(value), 2010, 2020)


def audit_expiration(value):
    return len(value) == 4 and range_check(int(value), 2020, 2030)


def audit_height(value):
    if len(value) < 4:
        return False
    
    measure = int(value[:-2])
    unit = value[-2:]
    return unit in ["cm", "in"] and range_check(measure, 150, 193) if unit == "cm" else range_check(measure, 59, 76)


def audit_haircolor(value):
    import string
    return value[0] == '#' and all(_ in string.hexdigits for _ in value[1:])


def audit_eyecolor(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def audit_passportid(value):
    return len(value) == 9 and value.isdecimal()


def audit_countryid(value):
    return True


def audit_field(key, value):
    return switcher.get(key)(value)


switcher = {
    'byr': audit_birthdate,
    'iyr': audit_issuedate,
    'eyr': audit_expiration,
    'hgt': audit_height,
    'hcl': audit_haircolor,
    'ecl': audit_eyecolor,
    'pid': audit_passportid,
}


def diff(list1, list2):
    return [i for i in list1 + list2 if i not in list1 or i not in list2]


def is_valid(passport, detailed=False):
    if detailed:
        for key, value in passport.items():
            if not audit_field(key, value):
                return 0
        
        return 1

    return 1 if len(passport) == len(required) else 0


def passports(data, detailed=False):
    valid = 0
    passports = []
    current = {}

    for str in data:
        if not str:
            if len(diff(list(current.keys()), required)) == 0:
                valid += is_valid(current, detailed)

            current.clear()
            continue

        for fields in str.split():
            entry = fields.split(':')
            if entry[0] not in optional:
                current[entry[0]] = entry[1]

    valid += is_valid(current, detailed)

    return valid


def second():
    data = DataAnalyzer.text("2020/day4.txt")
    print("(4.2) valid passports {:d}".format(passports(data, True)))


def first():
    data = DataAnalyzer.text("2020/day4.txt")
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
