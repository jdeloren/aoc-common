import sys, re, math
from typing import List
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2023/day3.txt")

test_data = ['467..467..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..']

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

    import itertools
    return sum(list(itertools.chain(*numbers)))

def second():
    print(f"(2023 3.0) score => {interpret(test_data)}")
    print(f"(2023 3.1) score => {interpret(input)}")

def first():
    print(f"(2023 3.0) score => {interpret(test_data)}")
    print(f"(2023 3.1) score => {interpret(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
