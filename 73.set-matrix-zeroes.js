/*
 * @lc app=leetcode id=73 lang=javascript
 *
 * [73] Set Matrix Zeroes
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
  let zeroRows = new Set()
  let zeroColumns = new Set()
  matrix.map((row,i)=>{
    matrix[i].map((column,j)=>{
      if (matrix[i][j] === 0) {
        zeroRows.add(i)
        zeroColumns.add(j)
      }
    })
  })

  for (let i=0;i<matrix.length;i++) {
    if (zeroRows.has(i)) {
      matrix[i] = (new Array(matrix[0].length)).fill(0)
    } else {
      for (let j=0;j<matrix[i].length;j++) {
        if (zeroColumns.has(j))
        matrix[i][j] = 0
      }
    }
  }
};
// @lc code=end
