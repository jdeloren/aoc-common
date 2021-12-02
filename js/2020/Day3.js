const {DataAnalyzer} = require('../common/DataAnalyzer.js')
let data = DataAnalyzer.strs("2020/day3.txt")


function tree(data, x, y) {
    return data[x][y] === '#' ? 1 : 0;
}

function calc(x=0, y=0, i=3, j=1) {
    trees = tree(data, x, y)
    while (x + j < data.length) {
        x += j;
        y = (y + i) % data[x].length;
        trees += tree(data, x, y)
    }

    return trees;
}

function one() {
    answer = calc()
    console.log("(2020.3.1): " + answer)
}

function two() {
    answer = 1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    
    slopes.forEach(slope => {
        answer *= calc(0, 0, slope[0], slope[1])
    });

    console.log("(2020.3.2): " + answer)
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
}