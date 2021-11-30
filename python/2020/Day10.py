import sys
from common import DataAnalyzer


def splits(data, boundary = 16, prefix=""):
    data.sort()
    bundles = []

    n = 0
    i = boundary

    while i < len(data):
        scan = True
        if data[i]-3 == data[i-1]:
            bundles.append(data[n:i])
            n = i
        else:
            v = 1
            while scan and i+v < len(data):
                if data[i+v]-3 == data[i+v-1]:
                    bundles.append(data[n:i+v])
                    n = i+v
                    scan = False
                else:
                    v += 1

        i += boundary

    bundles.append(data[n:])
    answer = 1
    for j in range(len(bundles)):
        rating = 0 if j == 0 else bundles[j][0]
        answer *= (len(combinations(bundles[j], rating, [], [])))

    print("{:s} total combinations: {:}".format(prefix, answer))


def combinations(data, rating, listing, current):
    if max(data) in current and current not in listing:
        listing.append(current)
    else:
        copy = [x for x in data if x > rating and x < rating + 4]
        for i in range(1, 4):
            if rating+i in copy:
                transfer = current.copy()
                transfer.append(copy[copy.index(rating+i)])
                combinations(data, rating+i, listing, transfer)
        
    return listing


def joltage(data, rating=0):
    jolts = data.sort()
    differences = {1: [], 3: []}

    for i in range(len(data)):
        differences[data[i] - rating].append(data[i])
        rating = data[i]

    differences[3].append(max(data) + 3)
    return differences


def second():
    splits(DataAnalyzer.ints("2020/day10.txt"), 15, "(10.2)")


def print1(prefix, data):
    print("{:s}: 1: {:d}, 3: {:d}  => {:d} ".format(prefix, len(data[1]), len(data[3]), len(data[1]) * len(data[3])))


def first():
    print1("(10.1.00)", joltage([16,10,15,5,1,11,7,19,6,12,4]))
    print1("(10.1.01)", joltage([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]))
    print1("(10.1)", joltage(DataAnalyzer.ints("2020/day10.txt")))


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
