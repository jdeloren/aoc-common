def solve(puzzle, first, second):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
