#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None]*n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        sublist = self.arr[self.pointer:]
        end = self.pointer + (sublist.index(None) if None in sublist else len(self.arr))
        chunk = self.arr[self.pointer:end]
        self.pointer = end
        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

