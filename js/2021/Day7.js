const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.intcsv("2021/day7.txt")

function uno(x, y) { return Math.abs(y-x) }

function pos(x, y) { return [...Array(Math.abs(y - x)).keys()].reduce((sum, x) => sum+x+1, 0) }

function calc(cost, least=999999999, position=-1) {
    for (let i = 0; i < data.length; ++i) {
        let sum = data.reduce((sum, x) => sum + cost(i, x), 0)

        if (sum < least) {
            position = i, least = sum
        }
    }

    return [least, position]
}

function one() {
    console.log("(2021.7.1): " + calc(uno))
}

function two() {
    console.log("(2021.7.2): " + calc(pos))
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
