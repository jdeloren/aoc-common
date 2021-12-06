const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2021/day6.txt")


function build() {
    fish = new Map()
    for (let i = 0; i <= 8; ++i) { fish[i] = 0 }
    return fish
}

function meta(input, days, length=5000000, cycle=6, birth=8) {
    let school = build()
    input.forEach(x => { school[x] ++ })
    
    for (let i = 0; i < days; ++i) {
        let eggs = build()

        //WTH NOT WORKING??? school.forEach((count, age) => {
        for (let age = 0; age <= 8; ++age) {
            let count = school[age]
            if (age == 0) {
                eggs[cycle] += count, eggs[birth] += count
            }
            else {
                eggs[age - 1] += count
            }
        }

        school = eggs
    }

    let fish = 0
    for (let age = 0; age <= 8; ++age) { fish += school[age] }

    return fish
}

function one() {
    fish = []
    data[0].split(',').forEach(i => {fish.push(parseInt(i))})
    console.log("(2021.6.1): " + meta(fish, 80))
}

function two() {
    fish = []
    data[0].split(',').forEach(i => {fish.push(parseInt(i))})
    console.log("(2021.6.2): " + meta(fish, 256))
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
