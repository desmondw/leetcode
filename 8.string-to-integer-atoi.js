/*
 * @lc app=leetcode id=8 lang=javascript
 *
 * [8] String to Integer (atoi)
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
  s = s.trim()
  let sign = 1
  if (s[0] == '-' || s[0] == '+') {
    sign = s[0] == '-' ? -1 : 1
    s = s.slice(1)
  }
  if (!s.length || !/\d/.test(s[0])) return 0

  let resp = sign * parseInt(s.split(/[^\d]/)[0])
  return Math.min(2**31-1, Math.max(-(2**31), resp))
};
// @lc code=end

