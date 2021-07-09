#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        v = {'count': 0, 's': s}

        self.check_remove(v, 'IV', 4)
        self.check_remove(v, 'IX', 9)
        self.check_remove(v, 'XL', 40)
        self.check_remove(v, 'XC', 90)
        self.check_remove(v, 'CD', 400)
        self.check_remove(v, 'CM', 900)

        self.check_remove(v, 'I', 1)
        self.check_remove(v, 'V', 5)
        self.check_remove(v, 'X', 10)
        self.check_remove(v, 'L', 50)
        self.check_remove(v, 'C', 100)
        self.check_remove(v, 'D', 500)
        self.check_remove(v, 'M', 1000)

        return v['count']
        
    def check_remove(self, v, text, value):
        if text in v['s']:
            print(v)
            print(text)
            v['count'] += v['s'].count(text) * value
            v['s'] = v['s'].replace(text, '')

# @lc code=end
