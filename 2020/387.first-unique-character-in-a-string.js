/*
 * @lc app=leetcode id=387 lang=javascript
 *
 * [387] First Unique Character in a String
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
  s = [...s]
  let unique = s.filter(v=>s.indexOf(v)==s.lastIndexOf(v))
  return unique.length ? s.indexOf(unique[0]) : -1
};
// @lc code=end

