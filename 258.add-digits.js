/*
 * @lc app=leetcode id=258 lang=javascript
 *
 * [258] Add Digits
 */

// @lc code=start
/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
  while ((num = [...`${num}`].reduce((a,v)=>a+ +v,0))>9) ;
  return num
};
// @lc code=end

