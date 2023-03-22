#
# @lc app=leetcode id=1629 lang=python3
#
# [1629] Slowest Key
#

# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        nTop = 0
        nC = 'a'

        start = 0
        for i in range(len(releaseTimes)):
            time = releaseTimes[i] - start
            if time >= nTop:
                if time == nTop:
                    nC = chr(max(ord(nC), ord(keysPressed[i])))
                else:
                    nC = keysPressed[i]
                nTop = time
            start = releaseTimes[i]
        return nC

# @lc code=end

