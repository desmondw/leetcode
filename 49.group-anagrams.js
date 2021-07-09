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
  let groups = {}
  for (let i=0;i<strs.length;i++) {
    let hash = [...strs[i]].sort().join('')
    groups[hash] = [...(groups[hash]||[]), strs[i]]
  }
  return Object.values(groups)
};


// @lc code=end

