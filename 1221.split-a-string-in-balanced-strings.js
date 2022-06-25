/*
 * @lc app=leetcode id=1221 lang=javascript
 *
 * [1221] Split a String in Balanced Strings
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
  if (s.length < 2) return 0

  let total = 0
  let counts = {
    R: 0,
    L: 0,
  }
  let char = null

  for (let i=0; i<s.length; i++) {
    if (!char) char = s[i]

    if (s[i] === char) counts[char]++
    else               counts[nonChar(char)]++

    let countsEqual = counts.R === counts.L
    let nextIsNewSeries = false
    if (countsEqual || nextIsNewSeries) {
      total++

      // reset
      counts.R = 0
      counts.L = 0
      char = null
    }
  }

  return total
};

function nonChar(c) {
  return c === 'L' ? 'R' : 'L'
}
// @lc code=end

