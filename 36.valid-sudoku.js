/*
 * @lc app=leetcode id=36 lang=javascript
 *
 * [36] Valid Sudoku
 */

// @lc code=start
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  let rowsValid = true
  let columnsValid = true
  let squaresValid = true
  for (let i=0;i<board.length;i++) {
    let column = []
    let square = []
    for (let j=0;j<board.length;j++) {
      column.push(board[j][i])

      let zy = ~~(i/3)*3
      let zx = i%3*3
      let y = zy + ~~(j/3)
      let x = zx + j%3
      square.push(board[x][y])
    }
    rowsValid = rowsValid && testUnique(board[i])
    columnsValid = columnsValid && testUnique(column)
    squaresValid = squaresValid && testUnique(square)
  }
  
  return rowsValid && columnsValid && squaresValid
};

function testUnique(arr) {
  arr = arr.filter(v=>v!='.')
  console.log(arr)
  return arr.join('') == [...new Set(arr)].join('')
}
// @lc code=end

