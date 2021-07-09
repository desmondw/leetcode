/*
 * @lc app=leetcode id=1461 lang=javascript
 *
 * [1461] Check If a String Contains All Binary Codes of Size K
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var hasAllCodes = function(s, k) {
  let sets = [...(new Array(2**k)).keys()]
  return sets.every(v=>s.includes(v.toString(2).padStart(k,'0')))
};
// @lc code=end

