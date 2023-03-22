/*
 * @lc app=leetcode id=922 lang=javascript
 *
 * [922] Sort Array By Parity II
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function(nums) {
  let output = Array(nums.length)
  let iEven = 0
  let iOdd = 1

  for (let i=0;i<nums.length;i++) {
    if (nums[i] % 2 === 0) {
      output[iEven] = nums[i]
      iEven += 2
    } else {
      output[iOdd] = nums[i]
      iOdd += 2
    }
  }

  return output
};
// @lc code=end

