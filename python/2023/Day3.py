import sys
import itertools
from typing import List
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2023/day3.txt")

test_data = [
            '467..467..',
            '...*...*..',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..'
        ]

def gears(data: List[str], NEWLINE = '\n'):
    read = lambda s: list(s.strip())
    schematic = list(map(read, data))

    def find_coordinates(sublist, i):
        coords = []
        for j, element in enumerate(sublist):
            if element == '*':
                coords.append((i, j))
        return coords

    stars = [c for c in list(map(find_coordinates, schematic, range(len(schematic)))) if c]
    stars = list(itertools.chain(*stars))

    def adjacent(a, b):
        x1, y1 = a
        x2, y2 = b
        return (abs(x1 - x2) == 1 and abs(y1 - y2) == 0) or \
            (abs(x1 - x2) == 0 and abs(y1 - y2) == 1) or \
            (abs(x1 - x2) == 1 and abs(y1 - y2) == 1)

    def locate(star, row_indeces):
        def gear_check(star, numbers):
            offset = 0
            count = []
            for number in numbers:
                start = ''.join(row).index(number, offset)
                for i in range(start, start+len(number)):
                    if adjacent((row_index, i), star):
                        count.append(int(number))
                        break

                offset = ''.join(row).index(number) + len(number)
            
            return count

        checks = []
        for row_index in row_indeces:
            row = schematic[row_index]
            numbers = [n for n in ''.join([c if c.isdigit() else '.' for c in row]).split('.') if n != '']
            checks.extend(gear_check(star, numbers))
        
        if len(checks) == 2:
            return checks[0] * checks[1]
        
        return 0
    
    def calc(star):
        gears = []
        if star[0] == 0:
            rows = [star[0], star[0]+1]
        elif star[0] == len(schematic)-1:
            rows = [star[0]-1, star[0]]
        else:
            rows = [star[0]-1, star[0], star[0]+1]
        
        gears.append(locate(star, rows))
        return sum(gears)   # yes, the sum of all gears i couldn't resist

    return sum(map(calc, stars))


def interpret(data: List[str], NEWLINE = '\n'):
    def symbol_hunt(index) -> List[int]:
        def number_hunt(marker, number):
            surrounding = []
            for i in range(marker, marker+len(number)):
                surrounding.extend([c for c in adjacent(index, i) if c != '.' and not c.isdigit()])
            
            return int(number) if len(surrounding) > 0 else None

        adjacent = lambda x, y: [schematic[i][j] for i in range(x-1, x+2) for j in range(y-1, y+2) if (i != x or j != y) and 0 <= i < len(schematic) and 0 <= j < len(schematic[0])]
        row = schematic[index]
        numbers = [n for n in ''.join([c if c.isdigit() else '.' for c in row]).split('.') if n != '']
        offset = 0
        adjacent_nums = []

        for number in numbers:
            adjacent_nums.append(number_hunt(''.join(row).index(number, offset), number))
            offset = ''.join(row).index(number) + len(number)
        
        return [n for n in adjacent_nums if n]

    read = lambda s: list(s.strip())
    schematic = list(map(read, data))
    numbers = list([n for n in map(symbol_hunt, range(len(schematic))) if n != []])

    return sum(list(itertools.chain(*numbers)))

def second():
    print(f"(2023 3.2) score => {gears(test_data)}")
    print(f"(2023 3.2) score => {gears(input)}")

def first():
    print(f"(2023 3.1) score => {interpret(test_data)}")
    print(f"(2023 3.1) score => {interpret(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
