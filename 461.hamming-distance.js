/*
 * @lc app=leetcode id=461 lang=javascript
 *
 * [461] Hamming Distance
 */

// @lc code=start
/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    return hammingWeight(x^y)
};
var hammingWeight = function(n) {
  let count = 0
  while (n>0) {
    if (n & 0b1) count++
    n = n >>> 1
  }
  return count
};
// @lc code=end

