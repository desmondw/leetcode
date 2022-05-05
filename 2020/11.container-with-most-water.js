/*
 * @lc app=leetcode id=11 lang=javascript
 *
 * [11] Container With Most Water
 */

// @lc code=start
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  let max = -Infinity
  for (let i=0;i<height.length;i++) {
    for (let j=i+1;j<height.length;j++) {
      let curVolume = (j-i)*Math.min(height[j],height[i])
      if (curVolume > max) max = curVolume
    }
  }
  return max
};
// @lc code=end

