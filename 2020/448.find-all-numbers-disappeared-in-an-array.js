/*
 * @lc app=leetcode id=448 lang=javascript
 *
 * [448] Find All Numbers Disappeared in an Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
  let resp = [...(new Array(nums.length)).keys()].map(v=>v+1)
  nums.forEach(v=>resp[v-1]=false)
  return resp.filter(v=>!!v)
};
// @lc code=end

