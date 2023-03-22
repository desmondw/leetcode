/*
 * @lc app=leetcode id=119 lang=javascript
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(idx) {
  // length = i + 1
  // pattern = 1, i, (i-1)*3 (i-1)*4

  //  1 4  6  4 1
  // 1 5 10 10 5 1
  //1 6 15 20 15 6 1
  if (idx === 0) return [1]
  let i = 1
  let arr = [1,1]
  while (i !== idx) {
    arr.unshift(1)
    for (let j=1; j<arr.length-1; j++) {
      arr[j] += arr[j+1]
    }
    i++
  }
  return arr
};
// @lc code=end

