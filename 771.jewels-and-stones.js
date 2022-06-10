/*
 * @lc app=leetcode id=771 lang=javascript
 *
 * [771] Jewels and Stones
 */

// @lc code=start
var numJewelsInStones = function(jewels, stones) {
  jewels = [...jewels]
  return [...stones].filter(v=>jewels.includes(v)).length
};
// @lc code=end

