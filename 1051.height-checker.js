/*
 * @lc app=leetcode id=1051 lang=javascript
 *
 * [1051] Height Checker
 */

// @lc code=start
/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
  let sorted = heights.slice().sort((a,b)=>a-b)
  let count = []
  for (let i=0;i<heights.length;i++){
    if (heights[i] !== sorted[i]) {
      let swapIdx = heights.lastIndexOf(sorted[i])
      let swap = heights[swapIdx]
      heights[swapIdx] = heights[i]
      heights[i] = swap
      count[i] = true
      count[swapIdx] = true
    }
  }
  return count.filter(v=>v===true).length
};
// @lc code=end

