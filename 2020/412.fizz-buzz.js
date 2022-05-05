/*
 * @lc app=leetcode id=412 lang=javascript
 *
 * [412] Fizz Buzz
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
  let lines = []
  for (let i=1;i<=n;i++){
    if (i%3==0 && i%5==0) {lines.push('FizzBuzz')}
    else if (i%3==0) {lines.push('Fizz')}
    else if (i%5==0) {lines.push('Buzz')}
    else {lines.push(''+i)}
  }
  return lines
};
// @lc code=end

