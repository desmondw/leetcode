/*
 * @lc app=leetcode id=49 lang=javascript
 *
 * [49] Group Anagrams
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
  let map = {}
  for (let i=0; i<strs.length; i++) {
    let str = strs[i]
    let strSort = [...str].sort().join('')
    map[strSort] = map[strSort] ? map[strSort] : []
    map[strSort].push(str)
  }

  return Object.values(map)
};
// @lc code=end

