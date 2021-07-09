/*
 * @lc app=leetcode id=71 lang=javascript
 *
 * [71] Simplify Path
 */

// @lc code=start
/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
  let stack = []
  path.split('/').map(v=>{
    if (v === '' || v === '.') return
    if (v === '..' && stack.length) stack.pop()
    if (v !== '..') stack.push(v)
  })
  return '/' + stack.join('/')
};
// @lc code=end

