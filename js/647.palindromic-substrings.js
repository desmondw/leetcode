/*
 * @lc app=leetcode id=647 lang=javascript
 *
 * [647] Palindromic Substrings
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
  let total = s.length

  // create hash map with char: indexes 'a': [0,2,6]
  let map = {}
  let v
  for (let i=0; i<s.length; i++) {
    v = s[i]
    map[v] = [...(map[v] || []), i]
  }

  // iterate over each index, and subsequent indexes,
  Object.entries(map).map(([char,indexes])=>{
    // and see if the substring between them is a palindrome
    for (let i=0; i < indexes.length; i++) {
      for (let j=i+1; j < indexes.length; j++) {
        let substr = s.substring(indexes[i], indexes[j]+1)
        if (substr === [...substr].reverse().join(''))
          total++
      }
    }
  })

  return total
};
// @lc code=end

