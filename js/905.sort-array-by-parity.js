/*
 * @lc app=leetcode id=905 lang=javascript
 *
 * [905] Sort Array By Parity
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
  return [...nums.filter(v=>v%2===0), ...nums.filter(v=>v%2)]
};
// @lc code=end

