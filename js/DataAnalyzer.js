class DataAnalyzer {

    static ints(path) {
        var fs = require('fs');
        var text = fs.readFileSync("../resources/" + path, "utf8").split('\n');

        return text.map( function(i) { return parseInt(i, 10) } );
    }

    static strs(path) {
        var fs = require('fs');
        var text = fs.readFileSync("../resources/" + path, "utf8").split('\n');

        return text.map( function(i) { return i } );
    }
}

exports.DataAnalyzer = DataAnalyzer
