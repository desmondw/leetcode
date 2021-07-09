/*
 * @lc app=leetcode id=1016 lang=javascript
 *
 * [1016] Binary String With Substrings Representing 1 To N
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} n
 * @return {boolean}
 */
var queryString = function(s, n) {
  for (let i=n;i>0;i--) {
    if (!s.includes(i.toString(2))) return false
  }
  return true
};
// @lc code=end

