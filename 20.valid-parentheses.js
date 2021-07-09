/*
 * @lc app=leetcode id=20 lang=javascript
 *
 * [20] Valid Parentheses
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let change = true
  while (change) {
    let s2=s.replace(/(\(\)|\{\}|\[\])/,'')
    change = s2!==s
    s=s2
  }
  return !s.length
};
// @lc code=end

