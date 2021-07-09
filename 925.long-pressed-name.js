/*
 * @lc app=leetcode id=925 lang=javascript
 *
 * [925] Long Pressed Name
 */

// @lc code=start
/**
 * @param {string} name
 * @param {string} typed
 * @return {boolean}
 */
var isLongPressedName = function(name, typed) {
  let freq = []
  ;[...typed].map(v=>{
    if (!freq.length || freq[freq.length-1][0] != v) freq.push([v,0])
    freq[freq.length-1][1]++
  })
  // console.log(freq)
  for (let i=0;i<name.length;i++){
    console.log(freq)
    console.log(name[i])
    if (!freq.length) return false
    if (freq[0][0] !== name[i]) {
      if (i-1 >= 0 && freq[0][0] === name[i-1]) {
        freq.shift()
        i--
        continue
      }
      return false
    }
    freq[0][1]--
    if ((freq[0][1]) === 0) freq.shift()
  }
  return freq.length === 0 || (freq.length === 1 && freq[0][0] === name[name.length-1])
}
// @lc code=end

