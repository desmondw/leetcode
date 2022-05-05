/*
 * @lc app=leetcode id=70 lang=javascript
 *
 * [70] Climbing Stairs
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
  let cache = []
  function climb(n) {
    if (cache[n]) return cache[n]
    if (n<3) return n
    cache[n] = climb(n-2) + climb(n-1)
    return cache[n]
  }

  return climb(n)
};
// @lc code=end

