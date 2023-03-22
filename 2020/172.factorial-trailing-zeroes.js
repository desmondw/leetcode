/*
 * @lc app=leetcode id=172 lang=javascript
 *
 * [172] Factorial Trailing Zeroes
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
  // if (n === 0) return 0
  // let total = 1
  // let zeroes = 0
  // for (let i=2;i<=n;i++) {
  //   total *= i

  //   // count and remove trailing zeroes
  //   while (total % 10 === 0) {
  //     total /= 10
  //     zeroes++
  //   }
  // }

  // console.log(total)
  // return zeroes
  return ~~(n/5)
};

// @lc code=end

