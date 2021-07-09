/*
 * @lc app=leetcode id=67 lang=javascript
 *
 * [67] Add Binary
 */

// @lc code=start
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
  a = [...a]
  b = [...b]
  let c = []
  let an, bn, carry=0, val
  while (a.length || b.length || carry) {
    an = a.length ? +a.pop() : 0
    bn = b.length ? +b.pop() : 0
    val = an+bn+carry
    c.unshift(val%2)
    carry = ~~(val/2)
  }
  return c.join('')
};
// @lc code=end

