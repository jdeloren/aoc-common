import sys
from collections import Counter
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2023/day7.txt")

test_data = [
'32T3K 765',
'T55J5 684',
'KK677 28',
'KTJJT 220',
'QQQJA 483'
]


five_of_a_kind = lambda x: len(set(x)) == 1
four_of_a_kind = lambda x: any(value == 4 for value in Counter(x).values())
full_house = lambda x: 2 in Counter(x).values() and 3 in Counter(x).values()
three_of_a_kind = lambda x: any(value == 3 for value in Counter(x).values())
two_pair = lambda x: list(Counter(x).values()).count(2) == 2
one_pair = lambda x: list(Counter(x).values()).count(2) == 1
hand_ranks = [lambda _: True, one_pair, two_pair, three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind]


def rank(hand: str, jokers=False):
    if jokers:
        wilds = lambda r, j: {
            0: {0: 0, 1: 1, 2: 3, 3: 5, 4: 6, 5: 6}, 
            1: {0: 1, 1: 3, 2: 5, 3: 6}, 
            2: {0: 2, 1: 4, 2: 5}, 
            3: {0: 3, 1: 5, 2: 6}, 
            4: {0: 4},
            5: {0: 5, 1: 6},
            6: {0: 6} 
        }[r].get(j, r)

        return [wilds(hand_ranks.index(r), hand.count('J')) for r in hand_ranks if r(hand.replace('J', ''))][-1]
    
    return [hand_ranks.index(r) for r in hand_ranks if r(hand)][-1]

def play(data, jokers=False):
    cards = 'J23456789TQKA' if jokers else '23456789TJQKA'
    from itertools import chain
    hands_and_bids = [d.split() for d in data]
    build_encoding = lambda x, y: list(chain([rank(x, jokers)], [cards.index(c) for c in x], [y]))
    encoded = sorted([build_encoding(hb[0], int(hb[1])) for hb in hands_and_bids])
    return sum((i+1) * h[-1] for i, h in enumerate(encoded))

def second():
    print(f"(2023 7.2) winnings => {play(test_data, jokers=True)}")
    print(f"(2023 7.2) winnings => {play(input, jokers=True)}")

def first():
    print(f"(2023 7.1) winnings => {play(test_data)}")
    print(f"(2023 7.1) winnings => {play(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
