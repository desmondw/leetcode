/*
 * @lc app=leetcode id=1441 lang=javascript
 *
 * [1441] Build an Array With Stack Operations
 */

// @lc code=start
/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function(target, n) {
  let output = []
  let diff = target[0] - 1
  output = addPushPop(output, diff)

  for (let i=1; i<target.length; i++) {
    diff = target[i] - target[i-1] - 1
    output = addPushPop(output, diff)
  }
  return output
};

let addPushPop = (arr, n) => {
  let add = ',Push,Pop'.repeat(n).slice(1).split(',')
  if (!add[0].length) add = []
  add.push('Push')
  return [...arr, ...add]
}
// @lc code=end

