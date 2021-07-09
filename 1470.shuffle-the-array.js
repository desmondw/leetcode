/*
 * @lc app=leetcode id=1470 lang=javascript
 *
 * [1470] Shuffle the Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
  let resp = []
  let j=0
  for (let i=0;i<n;i++) {
    resp[j] = nums[i]
    resp[j+1] = nums[i+n]
    j+=2
  }
  return resp
};
// @lc code=end

