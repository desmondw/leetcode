/*
 * @lc app=leetcode id=217 lang=javascript
 *
 * [217] Contains Duplicate
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  return !nums.every(v=>nums.indexOf(v)==nums.lastIndexOf(v))
};
// @lc code=end

