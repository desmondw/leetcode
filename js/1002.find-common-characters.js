/*
 * @lc app=leetcode id=1002 lang=javascript
 *
 * [1002] Find Common Characters
 */

// @lc code=start
/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
  words = words.map(word=>word.split('').sort().join('')).sort()
  console.log(words)

  let freq = {}
  words[0].split('').forEach(v=>{
    if (!freq[v]) freq[v] = 0
    freq[v]++
  })
  console.log(freq)

  for (let i=1; i<words.length; i++) {
    Object.entries(freq).forEach(([c, f])=>{
      for (let r=f; r>0; r--){
        if (!words[i].includes(c.repeat(r))) {
          freq[c]--
          if (freq[c] <= 0)
            delete freq[c]
        }
      }
    })
  }

  return Object.entries(freq).map(([c,f])=>c.repeat(f)).join('').split('')
};
// @lc code=end
