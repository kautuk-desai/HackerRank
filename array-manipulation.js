process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var n_temp = readLine().split(' ');
    var n = parseInt(n_temp[0]);
    var m = parseInt(n_temp[1]);
    var max = 0;
    var arr = new Array(n);
    arr.fill(0);
    for (var a0 = 0; a0 < m; a0++) {
        var a_temp = readLine().split(' ');
        var a = parseInt(a_temp[0]);
        var b = parseInt(a_temp[1]);
        var k = parseInt(a_temp[2]);
        if (k !== 0) {
            max = computeResult(arr, a - 1, b - 1, k, max);
        }
    }

    console.log(max);
}

function computeResult(arr, a, b, k, max) {
    for (let i = a; i <= b; i++) {
        arr[i] += k;
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}