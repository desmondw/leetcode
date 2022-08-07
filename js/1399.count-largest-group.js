/*
 * @lc app=leetcode id=1399 lang=javascript
 *
 * [1399] Count Largest Group
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
  let groups = []
  let sizes = Array(100).fill(0)
  for (let i=1;i<=n;i++){
    let sum = sumDigit(i)
    sizes[sum]++

    if (!groups[sum]) groups[sum] = []
    groups[sum].push(i)
  }
  sizes.sort((a,b)=>b-a) // could find max index instead
  console.log(sizes)
  return sizes.filter(v=>v===sizes[0]).length
};

function sumDigit(digit) {
  return (digit+'').split('').reduce((a,b)=>+b+a,0)
}
// @lc code=end

