/*
 * @lc app=leetcode id=190 lang=javascript
 *
 * [190] Reverse Bits
 */

// @lc code=start
/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
  let binary = Number(n).toString(2)
  binary = '0'.repeat(32-binary.length)+binary
  return parseInt([...binary].reverse().join(''),2)
};
// @lc code=end

