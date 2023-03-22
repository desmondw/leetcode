/*
 * @lc app=leetcode id=136 lang=javascript
 *
 * [136] Single Number
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  return nums.filter(v=>nums.indexOf(v)==nums.lastIndexOf(v))[0]
};
// @lc code=end

