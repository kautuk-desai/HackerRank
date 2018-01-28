/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
    nums = nums.sort(function (a, b) { return a - b; });
    var closest_sum = Infinity;
    var arr_len = nums.length;
    var ele1 = 0, start = 0, end = 0, sum = 0;

    for (let i = 0; i < arr_len - 2; i++) {
        ele1 = nums[i];
        start = i + 1;
        end = arr_len - 1;

        while (start < end) {
            sum = ele1 + nums[start] + nums[end];
            if (target === sum) {
                return sum;
            }
            else if (Math.abs(target - sum) < Math.abs(closest_sum - target) ) {
                closest_sum = sum;
            }
            else if (sum < target) {
                start++;
            }
            else {
                end--;
            }
        }
    }

    return closest_sum;
};
var arr = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6];
var result = threeSumClosest(arr, 26);
console.log(result);