/*
 * @lc app=leetcode id=240 lang=javascript
 *
 * [240] Search a 2D Matrix II
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
  while (matrix.length) {
    let row = matrix.shift()
    if (row[0] <= target && row[row.length-1] >= target) {
      if (binarySearch(row, target) !== -1) return true
    }
  }
  return false
};

function binarySearch(arr, v){
  let startIdx = 0
  let endIdx = arr.length - 1
  let midIdx = ~~((endIdx + startIdx)/2)

  while (arr[midIdx] !== v && startIdx < endIdx) {
    if      (v < arr[midIdx]) endIdx = midIdx - 1;
    else if (v > arr[midIdx]) startIdx = midIdx + 1;
    midIdx = ~~((endIdx + startIdx)/2)
  }

  return (arr[midIdx] !== v) ? -1 : midIdx;
}
// @lc code=end
