/*
 * @lc app=leetcode id=1646 lang=javascript
 *
 * [1646] Get Maximum in Generated Array
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
  if (n === 0) return 0
  let nums = [0, 1]
  for (let i=0;nums.length < n+1;i++) {
    nums[i*2] = nums[i]
    if (nums.length < n+1)
      nums[i*2+1] = nums[i] + nums[i+1]
  }
  console.log(nums)
  return Math.max(...nums)
};
// @lc code=end

