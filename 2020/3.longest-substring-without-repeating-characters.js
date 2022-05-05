/*
 * @lc app=leetcode id=3 lang=javascript
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let max = 0
  for (let i=0; i < s.length; i++) {
    let hash = {}
    let count = 0
    for (let j=i; j < s.length; j++) {
      if (hash[s[j]]) break
      hash[s[j]] = true
      count++
    }
    if (count > max) max = count
  }
  return max
};
// @lc code=end

