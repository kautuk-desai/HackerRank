/**
 * @param {number[]} nums
 * @return {number[][]}
 * test cases: empty array, array with all zero, array with numbers < 3, unique triplets.
 * Algo: 1. sort the array in increasing order
 * 2. if first element is > 0 return empty result
 * 3. else fix first element = ele1 of triplet and find other two elements using two sum method.
 * 4. repeat above step 3 until size - 1;
 */
var threeSum = function (nums) {
    var size = nums.length;
    nums = nums.sort(function (a, b) { return a - b });
    var ele = 0;
    var result = new Array();
    if (nums[0] > 0) {
        return result;
    }
    else {
        var triplets = new Array();
        var triplet_set = new Set();
        var set_ele = '';
        var sum = Infinity;
        var start = 0, end = 0;
        for (let i = 0; i < size - 1; i++) {
            ele = nums[i];
            start = i + 1;
            end = size - 1;
            while (start < end) {
                sum = ele + nums[start] + nums[end];
                if (sum === 0) {
                    set_ele = ele + '|' + nums[start] + '|' + nums[end];
                    if (!triplet_set.has(set_ele)) {
                        triplets.push(ele);
                        triplets.push(nums[start]);
                        triplets.push(nums[end]);
                        triplet_set.add(set_ele);
                    }
                    start++;
                    end--;
                }
                else if (sum < 0) {
                    start++;
                }
                else {
                    end--;
                }
            }
        }
    }

    var len = triplets.length;
    
    var triplet = new Array();

    for(let i = 0; i < len; i++){
        if((i+1)%3 === 0){
            triplet.push(triplets[i]);
            result.push(triplet);
            triplet = new Array();
        }
        else{
            triplet.push(triplets[i]);
        }
    }

    console.log(result);
};

threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]);