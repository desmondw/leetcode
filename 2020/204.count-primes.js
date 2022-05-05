/*
 * @lc app=leetcode id=204 lang=javascript
 *
 * [204] Count Primes
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
  let count = 0
  for (let i=2;i<n;i++) {
    if (checkPrime(i)) count++
  }
  return count
};

function checkPrime(n) {
  for (let i=2;i<=Math.sqrt(n);i++) {
    if (n%i == 0) return false
  }
  return true
}
// @lc code=end

