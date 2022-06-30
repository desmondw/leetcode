/*
 * @lc app=leetcode id=821 lang=javascript
 *
 * [821] Shortest Distance to a Character
 */

// @lc code=start
/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
  return [...s].map((l,i)=>{
    if (l === c) return 0

    let pre = s.slice(0,i).lastIndexOf(c)
    let post = s.slice(i+1).indexOf(c)
    pre = pre >= 0 ? i - pre : Infinity
    post = post >= 0 ? (i+post) - i + 1 : Infinity

    return Math.min(pre, post)
  })
};
// @lc code=end

