/*
 * @lc app=leetcode id=1337 lang=javascript
 *
 * [1337] The K Weakest Rows in a Matrix
 */

// @lc code=start
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function(mat, k) {
  let hash = {} // indexes, indexed by strength
  mat.forEach((row,i)=>{
    let strength = row.lastIndexOf(1)
    hash[strength] = [...(hash[strength]??[]), i]
  })
  let sorted = Object.entries(hash).sort((a,b)=>a[0]-b[0])
  sorted = sorted.map(v=>v[1])
  return sorted.flat().slice(0,k)
};
// @lc code=end

