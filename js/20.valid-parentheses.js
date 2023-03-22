/*
 * @lc app=leetcode id=20 lang=javascript
 *
 * [20] Valid Parentheses
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let matches = {
    '(': ')',
    '[': ']',
    '{': '}',
  }
  let stack = []
  for (let i=0; i<s.length; i++) {
    if (stack.length > 0 && matches[stack[stack.length-1]] === s[i])
      stack.pop()
    else
      stack.push(s[i])
  }
  return stack.length === 0
};
// @lc code=end

