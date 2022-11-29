import sys
from common import DataAnalyzer


def increment(v, tick=1):
    return v + tick

def reset(v, flashpoint):
    return v if v <= flashpoint else 0

def mprint(octopi):
    [print(''.join(map(str,v))) for v in octopi]
    print()

def cycler(octopi, steps=100, flashpoint=9, step=1, blinders=False):

    def flashing(octopi):
        blinks = set()
        for i in range(len(octopi)):
            for j in range(len(octopi)):
                if octopi[i][j] > flashpoint:
                    blinks.update([(i, j)])
        return blinks
    
    def flash(handled, blinking=set()):
        def stepper(x, y):
            try:
                if x >= 0 and y >= 0:
                    octopi[x][y] += step
            except:
                pass
        
        for x, y in blinking:
            stepper(x-1, y-1)
            stepper(x-1, y)
            stepper(x-1, y+1)
            stepper(x, y-1)
            stepper(x, y+1)
            stepper(x+1, y-1)
            stepper(x+1, y)
            stepper(x+1, y+1)

        return handled.symmetric_difference(flashing(octopi))
    
    def blinding():
        import itertools
        return all(x == 0 for x in itertools.chain(*octopi))


    flashes = 0
    counter = 0

    for _ in range(steps):
        counter += 1
        octopi = [[increment(j, step) for j in i] for i in octopi]

        handled = set()
        running = flashing(octopi)

        while len(running) > 0:
            handled = handled.union(running)
            running = flash(handled, running)
        
        octopi = [[reset(j, flashpoint) for j in i] for i in octopi]
        flashes += len(handled)

        if blinders and blinding():
            break
    
    return counter, flashes

def prep(input):
    values = [list(v) for v in input]
    return [[int(i) for i in v] for v in values]

def second():
    input = DataAnalyzer.text("2021/day11.txt")
    print(f"(11.2) blinding at step => {cycler(prep(input), 1000, blinders=True)[0]}")

def first():
    input = DataAnalyzer.text("2021/day11.txt")
    print(f"(11.1) total flashes => {cycler(prep(input))[1]}")


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
