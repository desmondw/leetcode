/*
 * @lc app=leetcode id=482 lang=javascript
 *
 * [482] License Key Formatting
 */

// @lc code=start
/**
 * @param {string} S
 * @param {number} K
 * @return {string}
 */
var licenseKeyFormatting = function(s,k) {
  s = s.replace(/-/g, '')
  let first = (s.length%k)||k
  let resp = []
  resp.push(s.slice(0,first))
  for (let i=first; i<s.length; i+=k) {
    resp.push(s.slice(i,i+k))
  }
  return resp.join('-').toUpperCase()
};
// @lc code=end

