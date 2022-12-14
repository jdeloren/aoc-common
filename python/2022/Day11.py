import sys
import math
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2022/day11.txt")
monkeys = []


class Monkey:   # ... that funky monkey!
    def __init__(self, identifier, modifier, additive, divisor, first, second, items, calming):
        self._id = identifier
        self._modifier = modifier
        self._divisor = divisor
        self._operation = self.add if additive else self.multiply
        self._first = first
        self._second = second
        self._items = items
        self._calming = calming
        self._inspections = 0
    
    def play(self, multiple=1):
        while len(self._items) > 0:
            self._inspections += 1
            item = int(self._items.pop(0))
            worry = self.inspect(item)
            worry = (worry // 3 if self._calming else worry % multiple)
            monkeys[self.throw(worry)].catch(worry)

    def inspect(self, worry):
        return self._operation(worry, self._modifier)

    def add(self, base, modifier):
        return base + modifier

    def multiply(self, base, modifier):
        return base * (modifier if modifier > 0 else base)

    def test(self, item):
        return item % self._divisor == 0
    
    def throw(self, item):
        return self._first if self.test(item) else self._second
    
    def catch(self, item):
        self._items.append(item)


def play(data, rounds, calming=True):
    global monkeys
    monkeys = []

    for i in range(0, len(data), 7):
        items = [x for x in data[i+1].split(':')[1].split(',')]
        try:
            modifier = int(data[i+2].split('=')[1].split(' ')[3])
        except ValueError:
            modifier = 0
        
        add = data[i+2].split('=')[1].split(' ')[2] == '+'
        divisor = int(data[i+3].split(' ')[-1])
        first = int(data[i+4].split(' ')[-1])
        second = int(data[i+5].split(' ')[-1])
        
        monkeys.append(Monkey(i // 7, modifier, add, divisor, first, second, items, calming))
    
    multiple = math.prod([m._divisor for m in monkeys])
    for _ in range(rounds):
        for m in monkeys:
            m.play(multiple)

    import heapq, numpy
    return numpy.prod(heapq.nlargest(2, [m._inspections for m in monkeys]))


def second():
    print(f"(2022 11.2) monkey business => {play(input, 10000, False)}")

def first():
    print(f"(2022 11.1) monkey business => {play(input, 20)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
