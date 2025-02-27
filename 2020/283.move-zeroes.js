/*
 * @lc app=leetcode id=283 lang=javascript
 *
 * [283] Move Zeroes
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  let numZeroes = nums.filter(v=>v==0).length
  for (let i=0;i<nums.length;i++){
    if (numZeroes == 0) break
    if (nums[i]==0) {
      nums.push(nums.splice(i,1))
      numZeroes--
      i--
    }
  }
};
// @lc code=end

