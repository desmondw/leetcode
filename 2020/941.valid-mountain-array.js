/*
 * @lc app=leetcode id=941 lang=javascript
 *
 * [941] Valid Mountain Array
 */

// @lc code=start
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
  if (arr.length <= 2) return false

  let maxIdx = arr.indexOf(Math.max(...arr))
  if (maxIdx === 0 || maxIdx === arr.length-1) return false
  for (let i=maxIdx+1; i<arr.length; i++) {
    console.log('a',i)
    if (arr[i] >= arr[i-1]) return false
  }
  for (let i=maxIdx-1; i>=0; i--) {
    console.log('b',i)
    if (arr[i] >= arr[i+1]) return false
  }
  return true
};
// @lc code=end

