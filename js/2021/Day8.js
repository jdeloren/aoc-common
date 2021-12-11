const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2021/day8.txt")

function basic() {
    let count = 0
    data.forEach(element => {
        datum = element.split(" | ")
        datum[1].split(" ").forEach(d => {
            switch(d.length) {
                case 2: // 1
                case 3: // 4
                case 4: // 7
                case 7: // 8
                    count++
            }
        })
    });

    return count
}

function full() {
    data.forEach(element => {
        let diag = ["zzzzzzzzz"]
        let key = {}, pre = {5: [], 6: []}, post = [], datum = element.split(" | ")
        // decode
        datum[0].split(" ").forEach(d => {
            switch(d.length) {
                case 2: // 1
                case 3: // 4
                case 4: // 7
                case 7: // 8
                    pre[d.length] = d
                    break
                case 5:
                case 6:
                    pre[d.length].push(d)
                    break
            }
        })

        console.log(pre)

        // generate
        datum[0].split(" ").forEach(d => {
        })
    })
}

function test() {
    data = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
    ]
    two()
}

function one() {
    console.log("(2021.7.1): " + basic())
}

function two() {
    console.log("(2021.7.2): " + full())
}


switch(process.argv.slice(2)[0]) {
    case '1':
        one()
        break

    case '2':
        test()
        break
    
    default:
        one()
        two()
}
