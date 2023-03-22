/*
 * @lc app=leetcode id=2 lang=javascript
 *
 * [2] Add Two Numbers
 */

class ListNode {
  constructor (val, next) {
      this.val = (val===undefined ? 0 : val)
      this.next = (next===undefined ? null : next)
  }
} 

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let addLargeNumbers = (str1, str2) => {

    let sum = "";  // our result will be stored in a string.
  
    // we'll need these in the program many times.
    let str1Length = str1.length;
    let str2Length = str2.length;
  
    // if s2 is longer than s1, swap them.
    if(str2Length > str1Length ){
        let temp = str2;
        str2 = str1;
        str1 = temp;
    }
  
    let carry = 0;  // number that is carried to next decimal place, initially zero.
    let a;
    let b;
    let temp;
    let digitSum;
    for (let i = 0; i < str1.length; i++) {
        a = parseInt(str1.charAt(str1.length - 1 - i));      // get ith digit of str1 from right, we store it in a
        b = parseInt(str2.charAt(str2.length - 1 - i));      // get ith digit of str2 from right, we store it in b
        b = (b) ? b : 0;                                    // make sure b is a number, (this is useful in case, str2 is shorter than str1
        temp = (carry + a + b).toString();                  // add a and b along with carry, store it in a temp string.
        digitSum = temp.charAt(temp.length - 1);            //
        carry = parseInt(temp.substr(0, temp.length - 1));  // split the string into carry and digitSum ( least significant digit of abSum.
        carry = (carry) ? carry : 0;                        // if carry is not number, make it zero.
  
        sum = (i === str1.length - 1) ? temp + sum : digitSum + sum;  // append digitSum to 'sum'. If we reach leftmost digit, append abSum which includes carry too.
  
    }
  
    return sum;     // return sum
  
  }
  
  let n1 = `${l1.val}`
  let n2 = `${l2.val}`
  while (l1.next) {
    l1 = l1.next
    n1 = l1.val + n1
  }
  while (l2.next) {
    l2 = l2.next
    n2 = l2.val + n2
  }

  // att()
  let n3 = addLargeNumbers(n1, n2)
  n3 = [...n3].map(v=>parseInt(v))
  let l3 = null
  let n = n3.shift()
  while (Number.isInteger(n)) {
    l3 = new ListNode(n, l3)
    n = n3.shift()
  }

  return l3
};
// @lc code=end


