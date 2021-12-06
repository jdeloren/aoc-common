const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2020/day7.txt")


function formulae() {

}

function calc() {
}

function test() {
    data = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags."
    ]
    formulae()
}

function one() {
    console.log("(2020.7): " + calc())
}

function two() {
    console.log("(2020.7): " + calc(matcher))
}

switch(process.argv.slice(2)[0]) {
    case '0':
        test()
        break
    
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