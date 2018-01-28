/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    var length = nums.length;
    let i = 0, j = 0, duplicates = 0;

    while (i < length && j < length) {
        if (nums[i] === nums[i + 1]) {
            j = i + 1;
            while (nums[j] === nums[j + 1] && j < length - 1) {
                j++;
            }
            if (nums[j + 1] !== undefined) {
                index = i + 1;
                while (index <= j) {
                    nums[index] = nums[j + 1];
                    index++;
                }
                i++;
            }
            else {
                length = i + 1;
                break;
            }
        }
        else {
            i++;
        }
    }

    console.log(nums);
    console.log(length);
    return length;
};
// var arr = [1, 1, 2, 2, 3, 4, 5, 9, 11, 15, 15];
// var arr = [1,1,2];
// var arr = [];
//var arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 12];
//var arr = [0,0,0,0,0,0,0,0,0,0,0];
//var arr = [0,1,2,3,4,5,6,7,8,9,10,20,30];
var arr = [-3,-1,-1,0,0,0,0,0,2];
removeDuplicates(arr);