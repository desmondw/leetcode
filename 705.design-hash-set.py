#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        self.size = 1000 # square root of max 10**6
        self.hashTable = [[None]*(self.size+1) for x in range((self.size+1))]

    def add(self, key: int) -> None:
        self.hashTable[key//self.size][key%self.size] = True

    def remove(self, key: int) -> None:
        self.hashTable[key//self.size][key%self.size] = False

    def contains(self, key: int) -> bool:
        return bool(self.hashTable[key//self.size][key%self.size])


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

