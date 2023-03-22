/*
 * @lc app=leetcode id=14 lang=javascript
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let i=0
    let prefix = ''
    while (strs.length && i < strs[0].length) {
      let valid = strs.every(v=>i < v.length && v[i]==strs[0][i])
      if (!valid) break
      prefix += strs[0][i]
      i++
    }
    return prefix
};
// @lc code=end

