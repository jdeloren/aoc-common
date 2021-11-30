import sys
from common import DataAnalyzer



def personal_seat(data):
    data.sort()
    previous = data[0] - 1
    answer = -1

    for n in data:
        if previous != n - 1 and previous != n:
            answer = n - 1
        
        previous = n
    
    return answer


def locator(str, low, hi, upper, lower):
    x = hi
    n = low

    for c in str:
        if c == upper:
            x -= ((x - n + 1) / 2)
        elif c == lower:
            n += ((x - n + 1) / 2)

    return int(n)


def seat_decoder(data):
    ids = []

    for str in data:
        row = locator(str[:-3], 0, 127, 'F', 'B')
        col = locator(str[-3:], 0, 7, 'L', 'R')

        ids.append(row*8 + col)
    
    return ids


def second():
    data = DataAnalyzer.text("2020/day5.txt")
    ids = seat_decoder(data)

    print("(5.2) your seat id: {:}".format(personal_seat(ids)))


def first():
    data = DataAnalyzer.text("2020/day5.txt")
    print("(5.1) max seat id: {:d}".format(max(seat_decoder(data))))


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
