/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
    nums = nums.sort(function (a, b) { return a - b });
    var arr_len = nums.length;
    var duplicates = 0;
    for (let i = 0; i < arr_len; i++) {
        if (nums[i] === val) {
            j = i;
            while (nums[j] === nums[j + 1] && j < arr_len) {
                j++;
                duplicates++;
            }
            j = j + 1;
            while (j < arr_len) {
                nums[i] = nums[j];
                i++;
                j++;
            }
            arr_len = arr_len - duplicates - 1;
            break;
        }
    }

    return arr_len;
};
// var arr = [1, 1, 2, 2, 3, 4, 5, 9, 11, 15, 15];
// var arr = [1,1,2];
// var arr = [];
//var arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 12];
var arr = [0,0,0,0,0,0,0,0,0,0,0];
//var arr = [0,1,2,3,4,5,6,7,8,9,10,20,30];
//var arr = [-3,-1,-1,0,0,0,0,0,2];
//var arr = [3,2,2,3];

var result = removeElement(arr, 0);
console.log(result);