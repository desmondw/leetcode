/*
 * @lc app=leetcode id=991 lang=javascript
 *
 * [991] Broken Calculator
 */

// @lc code=start
/**
 * @param {number} X
 * @param {number} Y
 * @return {number}
 */
var brokenCalc = function(x, y) {
  if (x > y) return x-y
  let ops = 0

  let lde = findLowestDoubleExponent(x,y)
  while ((x * 2**lde) > y) {
    x--
    ops++
  }
  if ((x * 2**lde) === y) return ops + lde
  else {
    x++
    ops--
  }

  return ++ops + brokenCalc(x*2,y)
};

// returns z such that
  // x * 2**(z-1) < y
  // x * 2**(z) >= y
function findLowestDoubleExponent(x,y) {
  // x * 2^z = y
  // 2^z = y / x
  // z * log2(2) = log2(y/x)
  // z = log2(y/x)
  let z = Math.log2(y/x)
  return Math.ceil(z)
}
// @lc code=end

