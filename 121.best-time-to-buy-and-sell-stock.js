/*
 * @lc app=leetcode id=121 lang=javascript
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let highest = prices[prices.length-1]
  let highestDiff = 0
  
  for (let i=prices.length-2;i>=0;i--) {
    if (prices[i] > highest) highest = prices[i]
    if (highest - prices[i] > highestDiff) highestDiff = highest - prices[i]
  }

  return highestDiff
};
// @lc code=end

