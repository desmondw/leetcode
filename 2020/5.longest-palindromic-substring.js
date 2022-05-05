/*
 * @lc app=leetcode id=5 lang=javascript
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  if (s.length == 1) return s
  let longest = ''
  for (let i=0; i<s.length; i++) {
    for (let j=i; j<s.length; j++) {
      if (j+1-i > longest.length && checkPalindrome(sub = s.slice(i,j+1))) {
        longest = sub
      }
    }
  }
  return longest
};

function checkPalindrome(s) {
  if (s.length == 1) return true
  let half = ~~(s.length/2)
  for (let i=0; i<=half; i++) {
    if (s[i] != s[s.length-1-i]) return false
  }
  return true
}
// @lc code=end

