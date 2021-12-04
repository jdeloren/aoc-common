const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2021/day4.txt")


function unmarked(board, marks) {
    let sum = 0
    for (let i = 0; i < board.length; ++i) {
        for (let j = 0; j < board[i].length; ++j) {
            if (marks[i][j] === 0) {
                sum += board[i][j]
            }
        }
    }

    return sum
}

function checker(row) {
    let sum = row.reduce((sum, x) => sum + x)
    return sum === row.length
}

function scan(call, board, marks) {
    for (let i = 0; i < board.length; ++i) {
        if (checker(marks[i])) {
            return call * unmarked(board, marks)
        }
        else {
            let col = []
            for (let j = 0; j < marks[i].length; ++j) {
                col.push(marks[j][i])
            }

            if (checker(col)) {
                return call * unmarked(board, marks)
            }
        }
    }

    return 0
}

function stamp(num, board, marks) {
    for (let i = 0; i < board.length; ++i) {
        for (let j = 0; j < board[i].length; ++j) {
            if (board[i][j] == num) {
                marks[i][j] = 1
            }
        }
    }
}

function bingo(squidgame = false) {
    numbers = data[0].split(',').map(x => parseInt(x))
    let boards = [], markers = []
    let i = -1, j = 0
    for (let n = 1; n < data.length; ++n, ++j) {
        if (data[n].length === 0) {
            ++i, j = -1, boards[i] = [], markers[i] = []
        } else {
            nums = data[n].split(/\s+/)
            let entries = []
            nums.forEach(x => {if (x.length > 0) { entries.push(parseInt(x)) }})
            boards[i][j] = entries
            markers[i][j] = new Array(entries.length).fill(0)
        }
    }

    let solved = []
    if (squidgame) {
        solved = new Array(boards.length).fill(false)
    }

    for (let x = 0; x < numbers.length; ++x) {
        for (let n = 0; n < boards.length; ++n) {
            if (squidgame || !solved[n]) {
                stamp(numbers[x], boards[n], markers[n])
                if (x > 3) {
                    let result = scan(numbers[x], boards[n], markers[n])
                    if (result > 0) {
                        if (squidgame) {
                            solved[n] = true
                        }
                        if (!squidgame || solved.every(x => x === true)) {
                            return result
                        }    
                    }
                }
            }
        }
    }
}

function one() {
    console.log("(2021.4.1): " + bingo())
}

function two() {
    console.log("(2021.4.2): " + bingo(true))
}


switch(process.argv.slice(2)[0]) {
    case '1':
        one()
        break

    case '2':
        two()
        break
    
    default:
        one()
        two()
}
