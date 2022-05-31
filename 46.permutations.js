/*
 * @lc app=leetcode id=46 lang=javascript
 *
 * [46] Permutations
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
  if (nums.length === 0) return [[]]
  
  let lists = []
  for (let i=0;i<nums.length;i++){
    let pseudoSplice = [...nums.slice(0,i), ...nums.slice(i+1)]
    let sublists = permute(pseudoSplice)
    sublists.forEach(list => {
      lists.push([nums[i], ...list])
    })
  }
  return lists
};
// @lc code=end

