/*
 * @lc app=leetcode id=1863 lang=javascript
 *
 * [1863] Sum of All Subset XOR Totals
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var subsetXORSum = function(nums, start=0) {
  let subsets = getAllSubsets(nums)
  return subsets.reduce((a,v)=>{
    return a + xorTotal(v)
  },0)
};

let xorTotal = (arr) => {
  if (arr.length === 0) return 0
  else if (arr.length === 1) return arr[0]
  return arr.slice(1).reduce((a,v)=>a^v,arr[0])
}

// let getSubsets = (nums, set=[])=>{
//   if (nums.length === 1)
//     return [[nums[0]]]

//   let ubersets = []
//   for (let i=1; i<nums.length; i++) {
//     let subsets = getSubsets(nums.slice(i))
//     console.log(subsets)
//     subsets = subsets.map(arr=>[nums[0], ...arr])
//     ubersets = [...ubersets, ...subsets]
//   }
//   return ubersets
// }

const getAllSubsets =
      theArray => theArray.reduce(
        (subsets, value) => subsets.concat(
         subsets.map(set => [value,...set])
        ),
        [[]]
      );
// @lc code=end

