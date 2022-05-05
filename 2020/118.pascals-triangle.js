/*
 * @lc app=leetcode id=118 lang=javascript
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
  let t = []
  for (let i=1;i<=numRows;i++) {
    let row = (new Array(i)).fill(1)

    if (i >= 3) {
      let prevRow = t[t.length-1]
      for (let j=1;j<row.length-1;j++) {
        row[j] = prevRow[j-1] + prevRow[j]
      }
    }
    t.push(row)
  }
  return t
};
// @lc code=end

