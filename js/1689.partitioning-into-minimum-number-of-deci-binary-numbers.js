/*
 * @lc app=leetcode id=1689 lang=javascript
 *
 * [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
 */

// @lc code=start
/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
  return +[...n].sort((a,b)=>b-a)[0]
};
// @lc code=end

