/*
 * @lc app=leetcode id=1910 lang=javascript
 *
 * [1910] Remove All Occurrences of a Substring
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
  const i = s.search(part)
  if (i === -1)
    return s
  return removeOccurrences(s.slice(0,i) + s.slice(i+part.length), part)
};
// @lc code=end

