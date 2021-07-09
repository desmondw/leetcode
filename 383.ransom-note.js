/*
 * @lc app=leetcode id=383 lang=javascript
 *
 * [383] Ransom Note
 */

// @lc code=start
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
  let freq = {}
  ;[...magazine].forEach(v=>{
    freq[v] = (freq[v]|0)+1
  })

  for (let i=0;i<ransomNote.length;i++) {
    let v = ransomNote[i]
    if (freq[v] > 0) freq[v]--
    else return false
  }
  return true
};
// @lc code=end

