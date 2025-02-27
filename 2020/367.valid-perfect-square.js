/*
 * @lc app=leetcode id=367 lang=javascript
 *
 * [367] Valid Perfect Square
 */

// @lc code=start
/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
  return Math.sqrt(num)%1 === 0
};
// @lc code=end

// 16 = 4^2
// log2(16) = 2 * log2(4)
// log2(16)/2 = log2(4)
// (log2(16)/2)^2 = 4