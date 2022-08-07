/*
 * @lc app=leetcode id=1475 lang=javascript
 *
 * [1475] Final Prices With a Special Discount in a Shop
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
  return prices.map((v,i)=>{
    let discount = prices.slice(i+1).find(v2=>v2<=v) || 0
    return v - discount
  })
};
// @lc code=end

