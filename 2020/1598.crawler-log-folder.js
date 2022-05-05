/*
 * @lc app=leetcode id=1598 lang=javascript
 *
 * [1598] Crawler Log Folder
 */

// @lc code=start
/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
  let count = 0
  logs.forEach(v=>{
    v = v.slice(0,-1)
    if (v === '..') {
      count = Math.max(0, count-1)
    } else if (v !== '.') {
      count++
    }
  })
  return count
};
// @lc code=end

