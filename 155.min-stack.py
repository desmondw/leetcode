#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.lowStack = []
        self.lowest = float('inf')

    def push(self, val: int) -> None:
        self.stack += [val]
        if val <= self.lowest:
            self.lowStack += [val]
            self.lowest = val

    def pop(self) -> None:
        if self.stack[-1] == self.lowStack[-1]:
            del self.lowStack[-1]
            self.lowest = self.lowStack[-1] if len(self.lowStack) else float('inf')
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.lowest



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

