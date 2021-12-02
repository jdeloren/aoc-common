const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2020/day4.txt")


function height(value) {
    data = value.slice(0, -2)
    if (value.endsWith('cm')) {
        return data >= 150 && data <= 193
    }
    else if (value.endsWith('in')) {
        return data >= 59 && data <= 76
    }

    return false
}

function strict(field, value) {
    switch(field) {
        case 'byr':
            return value >= 1920 && value <= 2002
        case 'iyr':
            return value >= 2010 && value <= 2020
        case 'eyr':
            return value.length === 4 && value >= 2020 && value <= 2030
        case 'hgt':
            return height(value)
        case 'hcl':
            return value[0] === '#' && value.length === 7 && /^[0-9a-f]+$/.test(value.slice(1))
        case 'ecl':
            return ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].includes(value)
        case 'pid':
            return !isNaN(parseInt(value)) && value.length === 9
        case 'cid':
            return true
    }

    return false
}

function blind(field, value) {
    return true
}


function check(passport, scan, required=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) {
    const all = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    let bank = required
    let fields = []

    passport.forEach(element => {
        let entry = element.split(':')
        if (scan(entry[0], entry[1])) {
            fields.push(entry[0])
        }
    })

    bank = bank.filter(field => !fields.includes(field))
    return bank.length === 0 ? 1 : 0
}

function calc(scan=blind) {
    passport = []
    valid = 0

    data.forEach(element => {
        if (element.length > 0) {
            passport.push(...(element.split(' ')))
        }
        else {
            valid += check(passport, scan)
            passport = []
        }
    });

    return valid
}

function one() {
    answer = calc()
    console.log("(2020.4.1): " + answer)
}

function two() {
    answer = calc(strict)
    console.log("(2020.4.2): " + answer)
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