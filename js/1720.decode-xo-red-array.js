/*
 * @lc app=leetcode id=1720 lang=javascript
 *
 * [1720] Decode XORed Array
 */

// @lc code=start
/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
  let arr = [first]
  for (let i=0;i<encoded.length;i++){
    let a = encoded[i]
    let b = arr[arr.length-1]
    arr.push(a^b)
  }
  return arr
};
// @lc code=end

