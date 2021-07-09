/*
 * @lc app=leetcode id=122 lang=javascript
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let total = 0
  let trough = prices[0]
  let peak = null
  for (let i=1;i<prices.length;i++) {
    if (prices[i-1] < prices[i]) peak = prices[i]
    if (prices[i-1] > prices[i]) {
      if (peak) {
        total += peak - trough
        peak = null
      }
      trough = prices[i]
    }
  }
  if (peak) {
    total += peak - trough
  }
  return total
};
// @lc code=end

