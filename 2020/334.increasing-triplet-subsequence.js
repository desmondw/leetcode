/*
 * @lc app=leetcode id=334 lang=javascript
 *
 * [334] Increasing Triplet Subsequence
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
  for (let i=0;i<nums.length;i++) {
    for (let j=i+1;j<nums.length;j++) {
      if (nums[i] < nums[j]) {
        for (let k=j+1;k<nums.length;k++) {
          if (nums[j] < nums[k]) return true
        }
      }
    }
  }
  return false
};
// @lc code=end

