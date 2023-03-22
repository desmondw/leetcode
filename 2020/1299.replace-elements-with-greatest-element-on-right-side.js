/*
 * @lc app=leetcode id=1299 lang=javascript
 *
 * [1299] Replace Elements with Greatest Element on Right Side
 */

// @lc code=start
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
  let max = -1
  for (let i=arr.length-1;i>=0;i--) {
    let swap = arr[i]
    arr[i] = max
    max = Math.max(max, swap)
  }
  return arr
};
// @lc code=end

