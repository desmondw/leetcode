/*
 * @lc app=leetcode id=709 lang=javascript
 *
 * [709] To Lower Case
 */

// @lc code=start
/**
 * @param {string} str
 * @return {string}
 */
var toLowerCase = function(str) {
  return [...str].map(v=>{
    let c = v.charCodeAt(0)
    if (65 <= c && c <= 90) c += 32
    return String.fromCharCode(c)
  }).join('')
};
// @lc code=end

