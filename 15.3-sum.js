/*
 * @lc app=leetcode id=15 lang=javascript
 *
 * [15] 3Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  let hash = {}
  nums.map((v,i)=>hash[v]=i)

  let triplets = new Set()

  for (let i=0;i<nums.length;i++) {
    for (let j=i+1;j<nums.length;j++) {
      let third = -(nums[i] + nums[j])
      if (third === -0) third = 0
      if (hash[third] !== undefined && hash[third] !== i && hash[third] !== j) {
        triplets.add([nums[i], nums[j], third].sort().join())
      }
    }
  }
  return [...triplets].map(v=>v.split(','))
};
// @lc code=end

