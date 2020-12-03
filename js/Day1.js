const {DataAnalyzer} = require('./DataAnalyzer.js')


function calc2(data, result=2020) {
    let set = new Set()
    set.add(data.shift())

    console.log(set)

    for (let i = 0; i < data.length; i++) {
        if (set.has(result - data[i])) {
            return [data[i], result - data[i]]
        }

        set.add(data[i])
    }

    return [-1, -1]
}

function calc3(data, result=2020) {
    for (let i = 0; i < data.length - 1; i++) {
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
    let data = DataAnalyzer.ints("2020/day1.txt")
    answer = calc2(data)
    console.log("(2020.1): " + answer[0] * answer[1])
}

function two() {
    let data = DataAnalyzer.ints("2020/day1.txt")
    answer = calc3(data)
    console.log("(2020.2): " + answer[0] * answer[1] * answer[2])
    console.log(answer)
}


switch(process.argv.slice(2)[0]) {
    case 1:
        one();
        break;

    case 2:
        two();
        break;
    
    default:
        one();
        two();
        break;
}