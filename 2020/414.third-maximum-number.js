/*
 * @lc app=leetcode id=414 lang=javascript
 *
 * [414] Third Maximum Number
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
  let resp = [...new Set(nums)].sort((a,b)=>b-a)
  return resp.length < 3 ? resp[0] : resp[2]
};
// @lc code=end

