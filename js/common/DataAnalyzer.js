const RESOURCE_ROOT = "../../resources/";

class DataAnalyzer {
    static ints(path) {
        var text = require('fs').readFileSync(RESOURCE_ROOT + path, "utf8").split('\n');
        return text.map( i => parseInt(i, 10) );
    }

    static strs(path) {
        return require('fs').readFileSync(RESOURCE_ROOT + path, "utf8").split('\n');
    }

    static intcsv(path) {
        let data = require('fs').readFileSync(RESOURCE_ROOT + path, "utf8").split('\n');
        let ints = []
        data[0].split(',').forEach(i => {ints.push(parseInt(i))})
        return ints
    }
}

exports.DataAnalyzer = DataAnalyzer
