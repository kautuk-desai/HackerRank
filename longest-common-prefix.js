/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    //console.log(strs[0].length);
    var num_strings = strs.length;
    if (num_strings < 1) {
        return "";
    }
    else if (num_strings === 1) {
        return strs[0];

    }
    else {
        var min_len = Infinity;
        for (let i = 0; i < num_strings; i++) {
            if (strs[i].length < min_len) {
                min_len = strs[i].length;
            }
        }

        var result = "";
        for (let i = 0; i < min_len; i++) {
            var is_match = checkCharacter(strs, num_strings, i);
            if (is_match) {
                result += strs[0][i];
            }
            else {
                break;
            }
        }

        return result;
    }
};
var checkCharacter = function (strs, num_strings, index) {
    for (let j = 0; j < num_strings - 1; j++) {
        if (strs[j][index] !== strs[j + 1][index]) {
            return false;
        }
    }
    return true;
}

var result = longestCommonPrefix(["a", "a", "b"]);
console.log(result);