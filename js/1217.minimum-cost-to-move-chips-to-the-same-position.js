/*
 * @lc app=leetcode id=1217 lang=javascript
 *
 * [1217] Minimum Cost to Move Chips to The Same Position
 */

// @lc code=start
/**
 * @param {number[]} position
 * @return {number}
 */
var minCostToMoveChips = function(position) {
  return Math.min(...position.reduce((a,v)=>{a[v%2]++; return a},[0,0]))
};
// @lc code=end

