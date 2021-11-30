import sys
from common import DataAnalyzer


def nesting(luggage, target):
    bags = 0

    del luggage[target] 
    for key, value in luggage.items():
        bags += value
    
    return bags


def pack(data, target, base=1, suitcase={}, depth=1):
    for key, value in data[target].items():
        if 'other' not in key:
            suitcase[key] = suitcase.get(key, 0) + value * base
            pack(data, key, value * base, suitcase, depth+1)
    
    return suitcase


def packer(file, target='shiny gold bag'):
    data = DataAnalyzer.text("2020/" + file)
    luggage = pack(patterns(data), target, 1, {target : 1})

    return nesting(luggage, target)


def options(data, target, current):
    for key, values in data.items():
        for k, v in values.items():
            if target == k:
                current.add(key)
                options(data, key, current)

    return current


def create_entry(data):
    return {'other bags': 0} if data == ['no other bag'] else {i[2:] : int(i[:2]) for i in data}


def patterns(data):
    patterns = {}

    for x in data:
        temp = x.replace('bags', 'bag').split('contain')
        patterns[temp[0][:-1]] = create_entry(temp[1][1:-1].split(', '))
    
    return patterns


def second():
    print("(7.2.0) {:d} bags inside shiny gold bag".format(packer('day0.txt')))
    print("(7.2.99) {:d} bags inside shiny gold bag".format(packer('day99.txt')))
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
