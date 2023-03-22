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
  strs.sort((a,b)=>a.length-b.length)
  console.log(strs)

  let prefix = strs[0] // starts at shortest
  if (prefix.length === 0) return ''

  for (let i=1; i<strs.length; i++) {
    for (let j=0; j<prefix.length; j++) {
      // if chars dont match, set new prefix
      if (prefix[j] != strs[i][j]) {
        prefix = prefix.slice(0,j)
        if (prefix.length === 0) return ''
        break
      }
    }
  }
  return prefix
};
// @lc code=end

