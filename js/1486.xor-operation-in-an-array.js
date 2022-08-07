/*
 * @lc app=leetcode id=1486 lang=javascript
 *
 * [1486] XOR Operation in an Array
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function(n, start) {
   let result = 0
   for (let i=start; i<start+n*2; i+=2) {
     result ^= i
   }
   return result
};
// @lc code=end

