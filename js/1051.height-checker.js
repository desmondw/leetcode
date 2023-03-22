/*
 * @lc app=leetcode id=1051 lang=javascript
 *
 * [1051] Height Checker
 */

// @lc code=start
/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
  let expected = heights.slice().sort((a,b)=>a-b)
  return heights.filter((v,i)=>v!==expected[i]).length
};
// @lc code=end

