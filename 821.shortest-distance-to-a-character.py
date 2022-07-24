#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idxs = [i for i,sc in enumerate(s) if sc == c]
        results = []
        for i in range(0, len(s)):
            if i in idxs:
                results.append(0)
                continue
            srt = idxs[:]
            srt.append(i)
            srt.sort()
            pos = srt.index(i)

            pre = float('inf') if pos == 0 else i - srt[pos-1]
            post = float('inf') if pos == len(srt)-1 else srt[pos+1] - i

            results.append(min(pre, post))

        return results
# @lc code=end

