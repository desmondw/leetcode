/*
 * @lc app=leetcode id=566 lang=javascript
 *
 * [566] Reshape the Matrix
 */

// @lc code=start
/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
  if (mat.length * mat[0].length !== r * c)
    return mat

  let flat = mat.reduce((a,b)=>{
    return [...a, ...b]
  }, [])

  let result = []
  for (let cr=0; cr < r; cr++) {
    result.push(flat.splice(0,c))
  }
  return result
};
// @lc code=end

