const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.ints("2020/day1.txt")

function calc2(result=2020) {
    let set = new Set()
    set.add(data.shift())

    for (let i = 0; i <= data.length; i++) {
        if (set.has(result - data[i])) {
            return [data[i], result - data[i]]
        }

        set.add(data[i])
    }

    return [-1, -1]
}

function calc3(result=2020) {
    for (let i = 0; i <= data.length - 1; i++) {
        let set = new Set()
        total = result - data[i]

        for (let j = i + 1; j < data.length; j++) {
            if (set.has(total - data[j])) {
                return [data[i], data[j], total - data[j]]
            }

            set.add(data[j])
        }
    }

    return [-1, -1, -1]
}

function one() {
    answer = calc2()
    console.log("(2020.1): " + answer[0] * answer[1])
}

function two() {
    answer = calc3()
    console.log("(2020.2): " + answer[0] * answer[1] * answer[2])
}


switch(process.argv.slice(2)[0]) {
    case '1':
        one();
        break;

    case '2':
        two();
        break;
    
    default:
        one();
        two();
        break;
}