/*
 * @lc app=leetcode id=415 lang=javascript
 *
 * [415] Add Strings
 */

// @lc code=start
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
  let size = Math.max(num1.length, num2.length)
  num1 = [...Array(size-num1.length).fill(0), ...num1.split('')]
  num2 = [...Array(size-num2.length).fill(0), ...num2.split('')]
  let carry = 0
  let result = Array(size)


  for (let i=size-1; i >= 0; i--) {
    let sum = +num1[i] + +num2[i] + carry
    result[i] = sum % 10
    carry = Math.floor(sum / 10)
  }
  if (carry > 0) result.unshift(carry)
  return result.join('')
};
// @lc code=end

