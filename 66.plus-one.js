/*
 * @lc app=leetcode id=66 lang=javascript
 *
 * [66] Plus One
 */

// @lc code=start
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    digits[digits.length-1] += 1
    if (digits[digits.length-1] == 10) {
      let slice = digits.slice(0,-1)
      if (slice.length == 0) slice = [0]
      digits = [...plusOne(slice), ...[0]]
    }
    return digits
};
// @lc code=end

