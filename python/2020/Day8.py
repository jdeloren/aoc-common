import sys
from common import DataAnalyzer


class Program:
    
    def duplicates(self, value):
        return value in self._executed


    def __init__(self, instructions, acc_default=0, max_depth=5000, debug=False):
        self._default_accumulator = acc_default

        self.instructions = instructions
        self.accumulator = self._default_accumulator
        self.terminator = self.duplicates
        self._terminated = False
        self._depth_exceeeded = False
        self.pointer = 0
        self.depth = max_depth
        self.debug = debug
        self._executed = []


    def __debug(self, value):
        self.debug = value


    def execute(self):
        if self.terminator is not None and self.terminator(self.pointer):
            print("TERMINATED on duplicate instruction: {:d}, {:d}".format(self.accumulator, self.pointer))
            self._terminated = True
            return

        if self.pointer >= len(self.instructions):
            self._terminated = True
            print("TERMINATED on pointer indexing: {:d} @ {:d}".format(self.pointer, self.accumulator))
            return

        self._executed.append(self.pointer)
        instruction = self.instructions[self.pointer]
        # print("PROCESSING {:s}".format(instruction))

        i = instruction.split(' ')
        command = i[0]
        value = int(i[1:][0])
        # print("MOD: {:d} from {:} is {:d} << {:d}".format(mod, i, value, int(i[1:][0])))

        if command == 'nop':
            print("NO-OP {:d}".format(value)) if self.debug else None
            self.pointer += 1
        elif command == 'acc':
            self.accumulator += value
            self.pointer += 1
            print("ACC {:d} => {:d} @ {:d}".format(value, self.accumulator, self.pointer)) if self.debug else None
        elif command == 'jmp':
            self.pointer += value
            print("JUMP {:d} => {:d}".format(value, self.pointer)) if self.debug else None
            self.execute()
        else:
            print("INVALID INSTRUCTION: {:s} {:}".format(command, value))
            self.pointer = -1


    def reset(self, instructions=[]):
        self.pointer = 0
        self.accumulator = self._default_accumulator
        self._executed.clear()
        self._terminated = False
        self._depth_exceeeded = False

        if instructions:
            self.instructions = instructions


    def run(self):
        self.reset()
        # print("START: {:} {:}".format(not self._terminated, len(self._executed) < self.depth))
        while not self._terminated and len(self._executed) < self.depth:
            self.execute()

        if len(self._executed) >= self.depth:
            self._depth_exceeeded = True
        

def modify(instructions, mod):
    modified = instructions.copy()
    while 'acc' in modified[mod]:
        mod += 1
        
    if 'nop' in modified[mod]:
        modified[mod] = modified[mod].replace('nop', 'jmp')
    else:
        modified[mod] = modified[mod].replace('jmp', 'nop')
    
    return mod+1, modified


def second():
    print("(8.2) program corruption detection algorithm")
    instructions = DataAnalyzer.text("2020/day8.txt")
    n, i2 = modify(instructions, 0)
    p = Program(i2)
    p.terminator = None
    p.run()

    if p._depth_exceeeded:
        while p._depth_exceeeded:
            n, i2 = modify(instructions, n)
            p.reset(i2)
            p.run()
    

def first():
    print("(8.1) program execution")
    p = Program(DataAnalyzer.text("2020/day8.txt"), 0)
    p.run()


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
