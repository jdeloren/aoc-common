import sys
from common import DataAnalyzer


def seat_check(data, i, j, x, y, extend=False):
    m = i + x
    n = j + y

    if n < 0 or n >= len(data) or m < 0 or m >= len(data[j]):
        return 0

    if extend:
        while data[m][n] == '.':
            m += x
            n += y
            if n < 0 or n >= len(data) or m < 0 or m >= len(data[j]):
                return 0
    
    if n >= 0 and n <= len(data) and m >= 0 and m <= len(data[j]):
        return 1 if data[m][n] == '#' else 0
    
    return 0


def seat_locator(data, m, n, enhanced=False):
    total = seat_check(data, m, n, -1, -1, enhanced)
    total += seat_check(data, m, n, -1, 0, enhanced)
    total += seat_check(data, m, n, -1, 1, enhanced)
    total += seat_check(data, m, n, 0, -1, enhanced)
    total += seat_check(data, m, n, 0, 1, enhanced)
    total += seat_check(data, m, n, 1, -1, enhanced)
    total += seat_check(data, m, n, 1, 0, enhanced)
    return total + seat_check(data, m, n, 1, 1, enhanced)


def iterate(data, enhanced=False, rounds=2000):
    i = len(data[0])
    j = len(data)
    max_occupy = 5 if enhanced else 4

    for zz in range(rounds):
        next = []
        changed = False

        for m in range(j):
            str = ''
            for n in range(i):
                if data[m][n] != '.':
                    total = seat_locator(data, m, n, enhanced)
                    
                    if data[m][n] == 'L' and total == 0:
                        str += '#'
                        changed = True
                    elif data[m][n] == '#' and total >= max_occupy:
                        str += 'L'
                        changed = True
                    else:
                        str += data[m][n]
                else:
                    str += '.'

            next.append(str)
        
        data = next

        occupied = 0
        for m in range(j):
            for n in range(i):
                occupied += 1 if next[m][n] == '#' else 0
            #     print(next[m][n], end='')
            # print('')
        if not changed:
            print("ROUND: {:d}, OCCUPIED: {:d}".format(zz+1, occupied))
            return


def second():
    data = DataAnalyzer.text("2020/day11.txt")
    iterate(data, True)


def first():
    data = DataAnalyzer.text("2020/day11.txt")
    iterate(data)


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
