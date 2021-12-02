const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.ints("2021/day1.txt")

function basic(numbers=data) {
    let count = 0
    for (let i = 1; i <= numbers.length; ++i) {
        if (numbers[i-1] < numbers[i]) {
            count++
        }
    }
    return count
}

function builder() {
    let numbers = []
    for (let i = 0; i < data.length-2; ++i) {
        numbers.push(data[i] + data[i+1] + data[i+2])
    }
    
    return basic(numbers)
}

function one() {
    answer = basic()
    console.log("(2021.1.1): " + answer)
}

function two() {
    answer = builder()
    console.log("(2021.1.2): " + answer)
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
