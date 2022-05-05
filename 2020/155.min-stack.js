/*
 * @lc app=leetcode id=155 lang=javascript
 *
 * [155] Min Stack
 */

// @lc code=start
/**
 * initialize your data structure here.
 */
var MinStack = function() {
  this.vals = []
  this.min = null
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
  this.min = this.min == null ? x : Math.min(this.min, x)
  this.vals.push(x)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  let popped = this.vals.pop()
  if (this.vals.length == 0) this.min = null
  else if (this.min == popped) this.min = Math.min(...this.vals)
  return popped
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  return this.vals[this.vals.length-1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
  return this.min
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
// @lc code=end

