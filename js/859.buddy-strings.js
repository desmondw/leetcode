/*
 * @lc app=leetcode id=859 lang=javascript
 *
 * [859] Buddy Strings
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var buddyStrings = function(s, goal) {
  if (s.length !== goal.length) return false
  if (s === goal) {
    s = [...s].sort()
    for (let i=1; i<s.length; i++) {
      if (s[i-1] === s[i]) return true
    }
    return false
  }

  let badIndexes = []
  for (let i=0; i<s.length; i++) {
    if (s[i] !== goal[i]) {
      badIndexes.push(i)
      if (badIndexes.length > 2) return false
    }
  }

  if (badIndexes.length !== 2) return false

  let [i1, i2] = badIndexes
  let a = s[i1]
  let b = s[i2]
  s = s.slice(0, i1) + b + s.slice(i1+1, i2) + a + s.slice(i2+1)
  return s === goal
};
// @lc code=end

