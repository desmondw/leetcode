/*
 * @lc app=leetcode id=1920 lang=javascript
 *
 * [1920] Build Array from Permutation
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
  return nums.map(v=>nums[v])
};
// @lc code=end

