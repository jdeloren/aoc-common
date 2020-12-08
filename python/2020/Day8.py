import sys
from common import DataAnalyzer



class Program:

    def __init__(self, instructions, acc_default=0, max_depth=50, debug=False):
        self.instructions = instructions
        self.accumulator = acc_default
        self.pointer = 0
        self.depth = max_depth
        self.debug = debug

        self.switcher = {
            'nop': exec_noop,
            'acc': exec_acc,
            'jmp': exec_jmp,
        }


        def __debug(self, value):
            self.debug = value


        def exec_noop(self, value):
            print("NO-OP {:d}".format(value)) if self.debug else pass
            pass


        def exec_acc(self, value):
            print("ACC {:d}".format(value)) if self.debug else pass
            self.accumulator += value


        def exec_jmp(self, value):
            print("JUMP {:d}".format(value)) if self.debug else pass
            self.pointer += value


        def instruction(self, command, value):
            return switcher.get(key)(value)
        

        def run(self):
            while self.pointer in range(0, len(self.instructions)):
                code = self.instructions[i]



def run_program(data):
    accumulator = 0

    for inst in data:
        pieces = inst.split(' ')
        mod = 1 if pieces[1][0] == '+' else -1
        instruction(pieces[0], mod * pieces[1:], accumulator)


def second():
    # print("(8.2) question count: {:d}".format(questions(data, audit_unique)))


def first():
    data = DataAnalyzer.text("2020/day8.txt")
    p = Program(DataAnalyzer.text("2020/day8.txt"), 0)
    p.run()
    # print("(8.1) question count: {:d}".format(questions(data)))


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
