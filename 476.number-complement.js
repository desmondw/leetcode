/*
 * @lc app=leetcode id=476 lang=javascript
 *
 * [476] Number Complement
 */

// @lc code=start
/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
  let binaryLength = num.toString(2).length
  let allOnes = parseInt('1'.repeat(binaryLength), 2)
  return num ^ allOnes
};
// @lc code=end

