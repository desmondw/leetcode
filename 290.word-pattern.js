/*
 * @lc app=leetcode id=290 lang=javascript
 *
 * [290] Word Pattern
 */

// @lc code=start
/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
  s = s.split(' ')
  if (pattern.length !== s.length) return false
  let patternValues = {}
  for (let i=0;i<pattern.length;i++) {
    let p = pattern[i]
    if (patternValues[p]) {
      if (patternValues[p] !== s[i]) return false
    } else patternValues[p] = s[i]
  }
  patternValues = Object.values(patternValues)
  return [...new Set(patternValues)].join() === patternValues.join()
}
// @lc code=end

