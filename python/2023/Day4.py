import sys
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2023/day4.txt")


test_data = [
'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]


def matches(card):
    parts = card.split(':')[1].split()
    winning = parts[:parts.index('|')]
    played = parts[parts.index('|')+1:]
    return id(card), [p for p in played if p in winning]

def id(card):
    return int(card.split(':')[0].split()[1])

def accumulate(cards):
    def scratch(card):
        id, matched = matches(card)
        return (id, list(range(id+1, id+1+len(matched))))

    winnings = dict(map(scratch, cards))
    ids = list(map(id, cards))

    total = len(cards)
    accumulated = [winner for id in ids for winner in winnings[id]]
    while len(accumulated) > 0:
        total += len(accumulated)
        accumulated = [winner for id in accumulated for winner in winnings[id]]

    return total

def play(data):
    _, matched = matches(data)
    return 0 if len(matched) == 0 else 2 ** (len(matched)-1)

def second():
    print(f"(2023 4.2) score => {accumulate(test_data)}")
    print(f"(2023 4.2) score => {accumulate(input)}")

def first():
    print(f"(2023 4.1) score => {sum(map(play, test_data))}")
    print(f"(2023 4.1) score => {sum(map(play, input))}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
