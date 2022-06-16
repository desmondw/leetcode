/*
 * @lc app=leetcode id=824 lang=javascript
 *
 * [824] Goat Latin
 */

// @lc code=start
/**
 * @param {string} sentence
 * @return {string}
 */
var toGoatLatin = function(sentence) {
  return sentence.split(' ').map((v,i)=>{
    if (!['a','e','i','o','u','A','E','I','O','U'].includes(v[0]))
      v = v.slice(1) + v[0]
    v += 'ma'
    v += 'a'.repeat(i+1)
    return v
  }).join(' ')
};
// @lc code=end

