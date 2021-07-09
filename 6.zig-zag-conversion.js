/*
 * @lc app=leetcode id=6 lang=javascript
 *
 * [6] ZigZag Conversion
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
  if (numRows < 2) return s
  let columns = []
  let rowIdx = 0, column
  while (s.length) {
    if (rowIdx == 0) {
      column = s.slice(0,numRows)
      s = s.slice(numRows)
    } else {
      column = [...' '.repeat(numRows)]
      column[rowIdx] = s[0]
      column = column.join('')
      s = s.slice(1)
    }
    columns.push(column)
    rowIdx--
    if (rowIdx < 0) rowIdx = numRows - 2
  }
  console.log(columns)

  let resp = ''
  for (let i=0;i<numRows;i++) {
    columns.map(v=>{
      resp += v[i] ? v[i] : ''
    })
  }
  return resp.replace(/\s/g,'')
};
// @lc code=end

