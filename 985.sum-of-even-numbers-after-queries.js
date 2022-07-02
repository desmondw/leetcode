/*
 * @lc app=leetcode id=985 lang=javascript
 *
 * [985] Sum of Even Numbers After Queries
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumEvenAfterQueries = function(nums, queries) {
  let answer = []
  for (let i=0;i<queries.length; i++) {
    [vali, indexi] = queries[i]
    nums[indexi] += vali
    let evenSum = nums.reduce((a,v)=>a+(v%2===0?v:0),0)
    console.log(evenSum)
    answer.push(evenSum)
  }
  return answer
};
// @lc code=end

