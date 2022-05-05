/*
 * @lc app=leetcode id=38 lang=javascript
 *
 * [38] Count and Say
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
  // if (n<10) return `${n}`
  let val = 1
  for (let i=1; i<n; i++) {
    val = expand(val)
  }
  return `${val}`
};

const expand = (n)=>{
  return `${n}`.replace(/([0-9])\1*/g, (match)=>{
    return +(match.length + match[0])
  })
}
// @lc code=end

