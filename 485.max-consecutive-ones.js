/*
 * @lc app=leetcode id=485 lang=javascript
 *
 * [485] Max Consecutive Ones
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
  let counts = []
  let count = 0
  nums.forEach(v=>{
    if (v === 0) {
      counts.push(count)
      count = 0
    }
    else count++
  })
  counts.push(count)
  return Math.max(...counts)
};
// @lc code=end

