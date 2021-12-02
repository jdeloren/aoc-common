const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2021/day2.txt")

function multiply(position) { return position[0] * [position[1]] }

function calc(aim=-1, processor=multiply, x=0, y=0) {
    pos = [x, y]
    data.forEach(d => {
        let cmd = d.split(" ")
        let unit = parseInt(cmd[1])
        if (cmd[0] === 'forward') {
            pos[0] += unit
            if (aim !== -1) {
                pos[1] += aim * unit
            }
        } else {
            let factor = (cmd[0] === 'up') ? -1 : 1
            if (aim !== -1) {
                aim += unit * factor
            } else {
                pos[1] += unit * factor
            }
        }
    })

    return processor(pos)
}

function one() {
    answer = calc()
    console.log("(2021.2.1): " + answer)
}

function two() {
    answer = calc(0)
    console.log("(2021.2.2): " + answer)
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
