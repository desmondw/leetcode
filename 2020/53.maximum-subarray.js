/*
 * @lc app=leetcode id=53 lang=javascript
 *
 * [53] Maximum Subarray
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  let max = -Infinity
  for (let i=0; i < nums.length; i++){
    let val = 0
    for (let j=i; j < nums.length; j++){
      if ((val += nums[j]) > max) {
        max = val
      }
    }
  }
  return max
};
// @lc code=end

