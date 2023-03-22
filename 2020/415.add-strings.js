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
  num1 = [...num1]
  num2 = [...num2]
  
  let value = ''
  let carry = 0
  while (num1.length || num2.length || !!carry) {
    let n1 = num1?.pop() ?? 0
    let n2 = num2?.pop() ?? 0
    
    let n3 = +n1 + +n2 + carry
    carry = ~~(n3/10)
    value = n3%10 + value
  }
  return value
};
// @lc code=end

