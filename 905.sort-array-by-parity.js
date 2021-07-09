/*
 * @lc app=leetcode id=905 lang=javascript
 *
 * [905] Sort Array By Parity
 */

// @lc code=start
/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {
  return [...A.filter(v=>v%2==0), ...A.filter(v=>v%2==1)]
};
// @lc code=end

