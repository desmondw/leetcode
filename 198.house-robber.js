/*
 * @lc app=leetcode id=198 lang=javascript
 *
 * [198] House Robber
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
  let cache = []

  for (let i=0;i<nums.length-3;i++){
    if (nums[i] == nums[i+1] && nums[i] == nums[i+2] && nums[i] == nums[i+3]) {
      nums.splice(i,1)
      i--
    }
  }

  function robd(nums, i=0) {
    console.log(cache)
    if (i >= nums.length) return 0

    if (!cache[i+2]) cache[i+2] = robd(nums, i+2)
    if (!cache[i+3]) cache[i+3] = robd(nums, i+3)
    
    return nums[i] + Math.max(cache[i+2], cache[i+3])
  }

  return Math.max(robd(nums, 0), robd(nums, 1))
};
// @lc code=end

