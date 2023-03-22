/*
 * @lc app=leetcode id=4 lang=javascript
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    nums = [...nums1, ...nums2].sort((a,b)=>a-b)
    if (nums.length%2==1) {
      return nums[~~(nums.length/2)]
    } else {
      return (nums[nums.length/2-1] + nums[nums.length/2]) / 2
    }
};
// @lc code=end

