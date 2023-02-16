#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = list(dict.fromkeys(key))
        if ' ' in key:
            key.remove(' ')
        return ''.join([chr(97+key.index(c)) if c != ' ' else ' ' for c in message])

# @lc code=end

