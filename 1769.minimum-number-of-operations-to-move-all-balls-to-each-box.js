/*
 * @lc app=leetcode id=1769 lang=javascript
 *
 * [1769] Minimum Number of Operations to Move All Balls to Each Box
 */

// @lc code=start
/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function(boxes) {
  boxes = [...boxes]
  let answer = []
  for (let i=0;i<boxes.length;i++) {
    let pre  = sum(boxes.slice(0,i).reverse())
    let post = sum(boxes.slice(i+1))
    answer.push(pre+post)
  }
  return answer
};

let sum = (arr)=>{
  if (!arr || arr.length == 0) return 0
  return arr.map((v,i)=>v*(i+1)).reduce((a,b)=>a+b)
}
// @lc code=end

