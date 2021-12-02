const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2020/day6.txt")


function counter(group) {
    let set = new Set()
    group.forEach(p => { p.forEach(item => set.add(item)) })

    return set.size
}

function matcher(group) {
    let set = [...group[0]]
    group.slice(0).forEach(p => {
        set = set.filter(x => p.includes(x))
    })

    return set.length
}

function calc(tabulator=counter) {
    let group = []
    let count = 0

    data.forEach(questions => {
        if (questions.length === 0) {
            count += tabulator(group)
            group = []
        }
        else {
            group.push(questions.split(''))
        }
    })

    return count + tabulator(group)
}

function one() {
    console.log("(2020.6.1): " + calc())
}

function two() {
    console.log("(2020.6.2): " + calc(matcher))
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