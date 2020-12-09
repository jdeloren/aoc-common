import sys
from common import DataAnalyzer


def nesting(luggage, target):
    bags = 0

    del luggage[target]
    for key, value in luggage.items():
        bags += value

    return bags


def pack(data, target, suitcase={}, depth=1):
    # print("TARGET: {:s} => {:}".format(target, suitcase))
    for value in data[target]:
        # print('CHECKING BAG: {:}'.format(value))
        count = 1 if value[0].isalpha() else int(value.split(' ')[0])
        style = target if value[0].isalpha() else value[2:]

        if 'no other' not in value:
            suitcase[style] = suitcase.get(style, 0) + (count * suitcase[target])
            pack(data, value[2:], suitcase, depth+1)
    
    return suitcase


def packer(file, target='shiny gold bag'):
    data = DataAnalyzer.text("2020/" + file)
    patterns(data)
    exit(0)
    luggage = pack(patterns(data), target, {target : 1})

    return nesting(luggage, target)


def options(data, target, current):
    check = []

    for key, values in data.items():
        for value in values:
            if target in value:
                current.add(key)
                options(data, key, current)

    return current


def create_entry(data):
    if ['no other bag'] == data:
        entry = {0: 'other bags'}
    else:
        entry = {}
        for i in data:
            entry[int(i[:2])] = i[2:]

    return entry


def patterns(data):
    patterns = {}

    for x in data:
        temp = x.replace('bags', 'bag').split('contain')
        patterns[temp[0][:-1]] = temp[1][1:-1].split(', ')
        # patterns[temp[0][:-1]] = create_entry(temp[1][1:-1].split(', '))
    
    return patterns


def second():
    # print("(7.2.0) {:d} bags inside shiny gold bag".format(packer('day0.txt')))
    # print("(7.2.99) {:d} bags inside shiny gold bag".format(packer('day99.txt')))
    print("(7.2) {:d} bags inside shiny gold bag".format(packer('day7.txt')))


def first():
    data = DataAnalyzer.text("2020/day7.txt")
    result = options(patterns(data), 'shiny gold bag', set())
    print("(7.1) {:d} patterns for {:s}".format(len(result), 'shiny gold bag'))


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
