/*
 * @lc app=leetcode id=746 lang=javascript
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(costs) {
  let cache = []
  
  function jump(costs, step) {
    if (step >= costs.length) return 0
    let cost = costs[step]
    
    if (!cache[step+1]) cache[step+1] = jump(costs, step+1)
    if (!cache[step+2]) cache[step+2] = jump(costs, step+2)
    let left = cache[step+1]
    let right = cache[step+2]
    
    return Math.min(cost + left, cost + right)
  }
  
  return Math.min(jump(costs,0), jump(costs,1))
};
// @lc code=end

