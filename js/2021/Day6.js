const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2021/day6.txt")


function meta(input, days, cycle=6, birth=8) {
    let school = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    input.forEach(x => { school[x] ++ })
    
    for (let i = 0; i < days; ++i) {
        let eggs = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

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

    return Object.values(school).reduce((sum, x) => sum + x)
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
