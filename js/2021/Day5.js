const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2021/day5.txt")


function calc(diag=false, size=999) {
    coords = []
    data.forEach(element => {
        items = []
        element.split(" -> ").forEach(x => x.split(',').forEach(y => items.push(parseInt(y))))
        coords.push(items)
    })

    let count = 0, grid = Array.from(Array(size), () => Array(size).fill(0))
    coords.forEach( x => {
        const a = x[0], b = x[1], c = x[2], d = x[3]
        if (a === c) {
            if (b > d) {
                for (let i = d; i <= b; ++i)
                    grid[i][a] += 1
            } else {
                for (let i = b; i <= d; ++i)
                    grid[i][a] += 1
            }
        } else if (b === d) {
            if (a > c) {
                for (let i = c; i <= a; ++i)
                    grid[b][i] += 1
            } else {
                for (let i = a; i <= c; ++i)
                    grid[b][i] += 1
            }
        } else if (Math.abs(a - c) === Math.abs(b - d)) {
            if (diag) {
                const f1 = a < c ? 1 : -1, f2 = b < d ? 1 : -1
                for (let n = 0, i = a, j = b; n <= Math.abs(a - c); n++, i += 1*f1, j += 1*f2) {
                    grid[j][i] += 1
                }    
            }
        }
    })

    grid.forEach(x => count += x.filter(i => i > 1).length)
    return count
}

function one() {
    console.log("(2021.5.1): " + calc())
}

function two() {
    console.log("(2021.5.2): " + calc(true))
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
