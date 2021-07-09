/*
 * @lc app=leetcode id=345 lang=javascript
 *
 * [345] Reverse Vowels of a String
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
  let vowels = [...s].filter(v=>'AEIOUaeiou'.includes(v))
  console.log(vowels)
  let resp = [...s]
  for (let i=0;i<s.length;i++) {
    if ('AEIOUaeiou'.includes(s[i])) resp[i] = vowels.pop()
  }
  return resp.join('')
};
// @lc code=end

