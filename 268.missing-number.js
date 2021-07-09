/*
 * @lc app=leetcode id=268 lang=javascript
 *
 * [268] Missing Number
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
  let n = (nums.length * (nums.length+1))/2
  return nums.reduce((a,v)=>a-v,n)
};
// @lc code=end

