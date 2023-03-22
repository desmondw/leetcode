/*
 * @lc app=leetcode id=350 lang=javascript
 *
 * [350] Intersection of Two Arrays II
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
  return nums1.filter(v=>{
    let idx = nums2.indexOf(v)
    if (idx >= 0) {
      nums2.splice(idx,1)
      return true
    }
    return false
  })
};
// @lc code=end

