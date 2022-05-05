/*
 * @lc app=leetcode id=946 lang=javascript
 *
 * [946] Validate Stack Sequences
 */

// @lc code=start
/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
  let iPush = iPop = 0
  let stack = []
  while (iPush < pushed.length && iPop < popped.length) {
    if (stack.length === 0 || !(stack[stack.length-1] === popped[iPop])) {
      stack.push(pushed[iPush])
      iPush++
    } else {
      stack.pop()
      iPop++
    }
  }
  return popped.slice(iPop).reverse().join() === stack.join()
};
// @lc code=end

