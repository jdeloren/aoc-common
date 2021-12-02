const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2020/day5.txt")


function checker(pass, lo, hi, start=0,end=127) {
    pass.split("").forEach(id => {
        if (id === lo) {
            end -= Math.floor((end-start+1)/2)
        } else {
            start += Math.floor((end-start+1)/2)
        }
    })

    return pass[pass.length-1] === hi ? end : start
}

function max(passes) {
    return Math.max(...passes)
}

function unique(passes) {
    let sorted = passes.sort((a, b) => a-b)
    let current = sorted[0]-1

    for (let i = 0; i < sorted.length; current = sorted[i], ++i) {
        if (sorted[i] !== current + 1) {
            return sorted[i]-1
        }
    }

    return -1
}

function calc(tabulator=max) {
    let passes = []
    data.forEach(pass => {
        row = checker(pass.slice(0, -3), 'F', 'B', 0, 127)
        col = checker(pass.slice(-3), 'L', 'R', 0, 7)
        passes.push((row*8)+col)
    })

    return tabulator(passes)
}

function one() {
    console.log("(2020.5.1): " + calc(max))
}

function two() {
    console.log("(2020.5.2): " + calc(unique))
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