/*
 * @lc app=leetcode id=88 lang=javascript
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
  let nums3 = [...nums1.slice(0,m), ...nums2].sort((a,b)=>a-b)
  for (let i=0;i<nums1.length;i++) {
    nums1[i] = nums3[i]
  }
};
// @lc code=end

