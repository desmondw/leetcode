/*
 * @lc app=leetcode id=856 lang=javascript
 *
 * [856] Score of Parentheses
 */

// @lc code=start
/**
 * @param {string} S
 * @return {number}
 */
var scoreOfParentheses = function(s) {
  s = s.replace(/\(\)/g, '1')
  console.log(s)

  let stack = 0
  let vals = []
  ;[...s].forEach((v,i)=>{
    if (v === '(') stack++
    else if (v === '1') vals.push(1)
    else {
      vals[vals.length-1] *= 2
    }
  })
  return vals.reduce((a,b)=>a+b,0)
};
// @lc code=end

