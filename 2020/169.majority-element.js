/*
 * @lc app=leetcode id=169 lang=javascript
 *
 * [169] Majority Element
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let freq = {}
  for (let i=0;i<nums.length;i++) {
    let v = nums[i]
    freq[v] = (freq[v]|0) + 1
    if (freq[v] > nums.length/2) return v
  }
  return false
};
// @lc code=end

