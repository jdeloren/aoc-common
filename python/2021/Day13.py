import sys
from common import DataAnalyzer

input = DataAnalyzer.text("2021/day13.txt")

test = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5',
    ''
]

def get_directions(data):
    coords = []
    folds = []
    x = y = -1

    for d in data:
        if ',' in d:
            mcfly = list(map(int, d.split(',')))
            coords.append((mcfly[0], mcfly[1]))
            x = max(x, mcfly[0])
            y = max(y, mcfly[1])
        elif len(d) > 0:
            i = d.index('=')
            folds.append((d[i-1], int(d[i+1:])))

    return coords, folds, x, y

def counter(paper):
    from collections import Counter
    counts = Counter(x for y in paper for x in y)
    return counts['#']

def ben(data, folds=5, scan=False, analyzer=counter):   #musicjokes
    import numpy as np

    marks, steps, x, y = get_directions(data)
    folds = folds if folds > 0 else len(steps)
    paper = [['.' for _ in range(x+1)] for _ in range(y+1)]

    cover = lambda i, j: '#' if i == '#' or j == '#' else '.'

    def mprint(octopi):
        [print(''.join(map(str,v))) for v in octopi]
        print()

    def fold(a, b):
        b = np.flipud(b)
        return [[cover(xx, yy) for xx, yy in zip(x, y)] for x, y in zip(a, b)]

    for i, j in marks:
        paper[j][i] = '#'
    
    # print(f'PAPER DIMENSIONS: {len(paper[0])} x {len(paper)}')
    paper = np.array(paper)

    for _, instruction in zip(range(folds), steps):
        if instruction[0] == 'x':
            rotated = np.rot90(paper, axes=(1, 0))
            cutline = instruction[1]
            # print(f'X CUT {cutline} {cutline+len(paper)%2} {len(rotated) % 2}')
            # mprint(rotated[:cutline])
            # mprint(rotated[cutline+len(paper)%2:])
            paper = fold(rotated[:cutline], rotated[cutline+len(paper[0])%2:])
            paper = np.rot90(paper)
        else:
            cutline = instruction[1]
            # print(f'Y CUT {cutline} {cutline+len(paper[0])%2} {len(paper) % 2}')
            # mprint(paper[:cutline])
            # mprint(paper[cutline+len(paper[0])%2:])
            paper = fold(paper[:cutline], paper[cutline+len(paper[0])%2:])
        # mprint(paper)
        # print(f"NEW SIZE: CUT {instruction[1]} {len(paper[0])} x {len(paper)}")
    
    if scan:
        mprint(paper)
    
    return analyzer(paper)

def second():
    print(f"(2021 13.2) scanned => {ben(test, folds=-1, scan=True)}")

def first():
    print(f"(2021 13.1) dots => {ben(input, folds=1)}")


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
