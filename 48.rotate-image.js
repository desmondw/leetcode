/*
 * @lc app=leetcode id=48 lang=javascript
 *
 * [48] Rotate Image
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(m) {
  console.log(m)
  for (let j=0;j<~~(m[0].length/2);j++) {
    let last = m[0].length-1
    for (let i=j;i<last-j;i++) {
      let swap = m[j][i]
      m[j][i] = m[last-i][j]
      m[last-i][j] = m[last-j][last-i]
      m[last-j][last-i] = m[i][last-j]
      m[i][last-j] = swap
    }
  }
};
// @lc code=end

