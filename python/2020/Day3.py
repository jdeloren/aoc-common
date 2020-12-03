import sys
from common import DataAnalyzer


def traverse(course, slope=[3,1], position=[0,0]):
    width = len(course[0])
    height = len(course)
    trees = 0

    while (position[0] + 1 < height):
        position[1] += slope[0]
        position[0] += slope[1]

        if position[1] >= width:
            position[1] = position[1] - width

        if course[position[0]][position[1]] == '#':
            trees +=1

    return trees


def second():
    data = DataAnalyzer.text("2020/day3.txt")
    count = 1
    for slope in [[1, 1],[3, 1],[5, 1],[7, 1],[1, 2]]:
        count *= traverse(data, slope, [0,0])
    
    print("(3.2) trees hit is {:d}".format(count))


def first():
    data = DataAnalyzer.text("2020/day3.txt")
    print("(3.1) trees hit is {:d}".format(traverse(data)))


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
