import sys
from common import DataAnalyzer


def survey(data, x, y):
    points = []
    if x > 0:
        points.append(data[x-1][y])
    if x+1 < len(data):
        points.append(data[x+1][y])
    if y > 0:
        points.append(data[x][y-1])
    if y+1 < len(data[0]):
        points.append(data[x][y+1])
    
    return data[x][y] < min(points)

def low_points(map):
    points = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if survey(map, i, j):
                points.append((i,j))

    return points

def trek(map, x, y, basin, max=9):
    basin.update([(x,y)])
    height = map[x][y]

    def height_check(i, j):
        return map[i][j] < max and height < map[i][j]

    if height < (max-1):
        if x > 0 and (x-1,y) not in basin and height_check(x-1, y):
            trek(map, x-1, y, basin)
        if x+1 < len(map) and (x+1,y) not in basin and height_check(x+1, y):
            trek(map, x+1, y, basin)
        if y > 0 and (x,y-1) not in basin and height_check(x, y-1):
            trek(map, x, y-1, basin)
        if y+1 < len(map[0]) and (x,y+1) not in basin and height_check(x, y+1):
            trek(map, x, y+1, basin)
    
    return basin

def basins(map, surveyor=low_points):
    basins = []
    points = surveyor(map)
    for p in points:
        basin = trek(map, p[0], p[1], set())
        basins.append(len(basin))
    
    import heapq, numpy
    return numpy.prod(heapq.nlargest(3, basins))

def score(map, surveyor=low_points):
    score = 0
    points = surveyor(map)
    for p in points:
        score += map[p[0]][p[1]] + 1
    
    return score

def input(data):
    out = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[i])):
            row.append(int(data[i][j]))
        out.append(row)

    return out


def second():
    values = DataAnalyzer.text("2021/day9.txt")
    map = input(values)
    print(f"(9.2) 2021 basin area => {basins(map)}")

def first():
    values = DataAnalyzer.text("2021/day9.txt")
    map = input(values)
    print(f"(9.1) 2021 risk level => {score(map)}")


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
