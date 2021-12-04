const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2021/day3.txt")


function oximeter(data, count) {
    return count > (data.length - count) ? '0' : '1'
}

function infrared(data, count) {
    return count <= (data.length - count) ? '0' : '1'
}

function filter(data, position, sensor) {
    if (data.length === 1) {
        return data
    } else {
        let bit = sensor(data, zeros(data, position))
        return data.filter(x => x[position] === bit)
    }
}

function zeros(data, i) {
    let zeros = 0
    for (let j = 0; j < data.length; ++j) {
        if (data[j][i] === '0') {
            zeros += 1
        }
    }

    return zeros
}

function life_support() {
    let oxygen = data, co2 = data

    for (let i = 0; i < data[0].length; ++i) {
        oxygen = filter(oxygen, i, oximeter)
        co2 = filter(co2, i, infrared)
    }

    return parseInt(oxygen[0], 2) * parseInt(co2[0], 2)
}

function power() {
    let threshold = parseInt(data.length / 2)
    let gamma = '', epsilon = ''

    for (let i = 0; i < data[0].length; ++i) {
        zero_count = zeros(data, i)
        gamma += zero_count >= threshold ? '0' : '1'
        epsilon += zero_count < threshold ? '0' : '1'
    }

    return parseInt(gamma, 2) * parseInt(epsilon, 2)
}

function one() {
    console.log("(2021.3.1): " + power())
}

function two() {
    console.log("(2021.3.2): " + life_support())
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
