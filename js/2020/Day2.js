const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2020/day2.txt")

function calc(interpreter=range) {
    let valid = 0;

    for (let i = 0; i <= data.length - 1; i++) {
        let entry = data[i];
        let tokens = entry.split(' ');
        let policy = tokens[0].split('-');

        valid += interpreter(policy[0], policy[1], tokens[1][0], tokens[2])
    }

    return valid;
}

function range(min, max, chr, passwd) {
    for (var n=count=0; n<passwd.length; count+=+(chr===passwd[n++]));
    if (count >= min && count <= max) {
        return 1;
    }

    return 0;
}

function pos(one, two, chr, passwd) {
    if (one > 0 && two > 0 && (passwd[one-1] === chr) !== (passwd[two-1] === chr)) {
        return 1;
    }

    return 0;
}

function one() {
    answer = calc()
    console.log("(2020.1): " + answer)
}

function two() {
    answer = calc(pos)
    console.log("(2020.2): " + answer)
}

switch(process.argv.slice(2)[0]) {
    case '1':
        one();
        break;

    case '2':
        two();
        break;
    
    default:
        one();
        two();
        break;
}