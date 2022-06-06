/*
 * @lc app=leetcode id=22 lang=javascript
 *
 * [22] Generate Parentheses
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n, open=0, str='') {
  if (n === 1) return ['()' + ')'.repeat(open)]

  let output = []
  for (let i=1; i <= n; i++){
    let subOutput1 = [], subOutput2 = []
    if (open > 0)
      subOutput1 = generateParenthesis(n, open-1, str+')') // closing paren
    subOutput2 = generateParenthesis(n-1, open+1, str+'(') // open paren

    output = [...output, ...subOutput1, ...subOutput2]
    // subOutputs = subOutputs.map(v=> v + ')')
    // output = [...output, ...subOutputs]
  }

  return output
};
// @lc code=end

