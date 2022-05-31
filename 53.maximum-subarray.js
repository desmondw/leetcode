/*
 * @lc app=leetcode id=53 lang=javascript
 *
 * [53] Maximum Subarray
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  
}

// var maxSubArray = function(nums) {
//   let best = -Infinity
//   let totals = []
//   for (let i=0;i<nums.length;i++){
//     totals.push(0)
//     totals = totals.map(v=>{
//       if (v+nums[i] > best) best = v+nums[i]
//       return v+nums[i]
//     })
//   }
  
//   return best
// };


// var maxSubArray = function(nums) {
//   let lValue = -Infinity
//   let memoized = []

//   let sum = 0
//   for (let i=0;i<nums.length;i++){
//     sum += nums[i]
//     if (sum > lValue) lValue = sum

//     let toSubtract = 0
//     for (let j=0;j<i;j++){
//       toSubtract += nums[j]
//       let v = sum - toSubtract
//       if (v > lValue) lValue = v
//     }
//   }
//   return lValue
// };
// @lc code=end
