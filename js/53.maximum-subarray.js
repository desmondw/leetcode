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
  if (nums.length === 0) return 0

  let sums = []
  let sum = nums[0]

  // pre-sum all positives and negatives
  for (let i=1; i<nums.length; i++) {
    if (Math.sign(nums[i-1]) !== Math.sign(nums[i])) {
      sums.push(sum)
      sum = 0
    }
    sum += nums[i]
  }
  sums.push(sum)

  // console.log(sums)

  if (sums.length === 1 && sums[0] < 0) {
    // only negatives
    return nums.sort((a,b)=>b-a)[0]
  }

  return checkForMax(sums)
}

// let checkForMax = function(sums) {
//   let best = -Infinity
//   let totals = []

//   let newVal
//   for (let i=0;i<sums.length;i++){
//     totals.push(0)
//     totals = totals.map(v=>{
//       newVal = v + sums[i]

//       if (newVal > best) best = newVal
//       return newVal
//     })
//   }
//   return best
// };

var checkForMax = function(nums) {
  let lValue = -Infinity
  let memoized = []

  let sum = 0
  for (let i=0;i<nums.length;i++){
    sum += nums[i]
    if (sum > lValue) lValue = sum

    let toSubtract = 0
    for (let j=0;j<i;j++){
      toSubtract += nums[j]
      let v = sum - toSubtract
      if (v > lValue) lValue = v
    }
  }
  return lValue
};






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
