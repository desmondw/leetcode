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
  let resp = new Array(s.length)
  let first = null
  let last = null
  ;[...s].map((v,i)=>{
    if (v !== c) return
    if (last === null) { first = last = i; return }
    
    let dist = 0
    do {
      resp[last+dist] = dist
      resp[i-dist] = dist
      dist++
    } while (resp[last+dist] === undefined)
    last = i
  })

  let dist = 0
  do {
    if (first-dist >= 0)      resp[first-dist] = dist
    if (last+dist < s.length) resp[last+dist] = dist
    dist++
  } while (first-dist >= 0 || last+dist < s.length)

  return resp
};
// @lc code=end

