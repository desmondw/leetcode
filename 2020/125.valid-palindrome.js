/*
 * @lc app=leetcode id=125 lang=javascript
 *
 * [125] Valid Palindrome
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  s = s.replace(/[^A-Za-z0-9]+/g,'').toLowerCase()
  return s == [...s].reverse().join('')
};
// @lc code=end

