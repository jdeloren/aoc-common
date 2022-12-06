import sys
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2022/day6.txt")[0]

def marker(signal, length=4):
    for i in range(0, len(signal)-length+1):
        check = signal[i:i+length]
        if len(set(check)) == length:
            return i+length, ''.join(check)
    
    return -1, ''

def second():
    print(f"(2022 6.2) large marker => {marker(input, 14)}")

def first():
    print(f"(2022 6.1) marker => {marker(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
