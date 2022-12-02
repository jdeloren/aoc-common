import sys
from common import DataAnalyzer

input = DataAnalyzer.text("2022/day2.txt")

def play(data, splashback=False):

    def hose_soaker(rounds):
        p1 = {'A' : 'R', 'B': 'P', 'C': 'S'}
        p2 = {'X' : 'R', 'Y': 'P', 'Z': 'S'}
        
        play = {'R' : 1, 'P': 2, 'S': 3}
        winners = ['RP', 'PS', 'SR']

        score = 0

        def spray(cpu, player):
            if player == 'Y':
                return cpu
            elif player == 'X':
                return {'R': 'S', 'P': 'R', 'S': 'P'}[cpu]

            return {'R': 'P', 'P': 'S', 'S': 'R'}[cpu]

        for i in rounds:
            a = p1[i[0]]
            b = p2[i[1]] if not splashback else spray(a, i[1])

            if a == b:
                score += play[b] + 3
            else:
                score += (play[b]) + (6 if a+b in winners else 0)

        return score

    return hose_soaker([d.split(' ') for d in data])  # enough with the hose!


def second():
    print(f"(2022 2.2) nothing beats that! => {play(input, splashback=True)}")

def first():
    print(f"(2022 2.1) good ol' rock => {play(input)}")


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
