/*
 * @lc app=leetcode id=492 lang=javascript
 *
 * [492] Construct the Rectangle
 */

// @lc code=start
/**
 * @param {number} area
 * @return {number[]}
 */
var constructRectangle = function(area) {
  let start = Math.ceil(Math.sqrt(area))
  for (let i=start; i<=area; i++) {
    if ((area/i)%1 === 0) return [i, area/i]
  }
};
// @lc code=end

