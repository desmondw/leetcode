/*
 * @lc app=leetcode id=371 lang=javascript
 *
 * [371] Sum of Two Integers
 */

// @lc code=start
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
  let carry;
  while((a & b) !== 0){
      carry = (a & b) << 1;
      a = a ^ b;
      b = carry;
  }
  return a ^ b;
};

// var getSum = function(a, b) {
//   // console.log(`a: 0b${a.toString(2)}`)
//   // console.log(`b: 0b${b.toString(2)}`)
//   let isSubtraction = false
//   let sign = 1
//   if (a < 0 && b < 0) sign = Math.sign(a)
//   else if (a < 0) isSubtraction = true
//   else if (b < 0) {
//     isSubtraction = true
//     let swap = a
//     a = b
//     b = swap
//   }
//   a = Math.abs(a)
//   b = Math.abs(b)
//   // if (isSubtraction) a = ~a
//   // isSubtraction = false
  
//   // console.log(isSubtraction)
//   console.log(`a ${a}: 0b${a.toString(2)}`)
//   console.log(`b ${b}: 0b${b.toString(2)}`)

//   let total = ''
//   let carry = Number(isSubtraction)
//   let sum, aVal
//   let i = 0
//   while (!(a===0 && b===0)) {
//     if (a===-1 && b===0) {
//       // TODO: something
//       total = `1${total}`
//       a = 0
//       continue
//     }
//     aVal = isSubtraction ? ~a&1 : a&1
//     // aVal = a&1
//     // console.log('aBit',aVal,'bBit',b&1,'carry',carry)

//     // console.log('--')
//     console.log('a',a,'b',b)
//     // console.log('a&1',a&1,'b&1',b&1)
//     ;[sum, carry] = fullAdder(aVal,b&1,carry)
//     // console.log('sum',sum,'carry',carry)
//     a >>>= 1
//     b >>>= 1
//     total = `${sum}${total}`
//     i++
//     // console.log('total',total)
//   }
//   console.log(i)
  
//   // console.log('--')
//   // console.log(`carry: 0b${carry}`)
//   // console.log(`sum: 0b${total}`)
//   // console.log(`0b${carry}${total}`)
//   carry = isSubtraction ? 0 : carry
//   console.log('carry',carry)
//   return parseInt(`${carry}${total}`,2) * sign
// };

// function fullAdder(a, b, c = 0) {
//   let abSum = a ^ b
//   let sum = abSum ^ c
//   let carry = (abSum & c) | (a & b)
//   // console.log('ADDBITS sum',sum,'carry',carry)
//   return [sum, carry]
// }
// @lc code=end

