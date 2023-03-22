/*
 * @lc app=leetcode id=541 lang=javascript
 *
 * [541] Reverse String II
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function(s, k) {
  let resp = ''
  let reverse = true
  for (let i=0;i<s.length;i+=k) {
    let substring = s.slice(i,i+k)
    if (reverse) substring = [...substring].reverse().join('')
    resp += substring
    reverse = !reverse
  }
  return resp
};
// @lc code=end

