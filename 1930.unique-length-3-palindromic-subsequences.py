#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pairs = {} # max length of 26

        # fill pairs with first/last indexes for each char
        for (i, c) in enumerate(s):
            if c not in pairs:
                pairs[c] = [i, -1]
            else:
                pairs[c][1] = i

        firstIdx = len(s)
        lastIdx = -1
        for c in list(pairs.keys()):
            if pairs[c][1] == -1:
                del pairs[c]
            else:
                # [chars between used]
                pairs[c].append([])
                if pairs[c][0] < firstIdx:
                    firstIdx = pairs[c][0]
                if pairs[c][1] > lastIdx:
                    lastIdx = pairs[c][1]

        # for indexes first..last:
        for i in range(firstIdx + 1, lastIdx):
            for pair in pairs.values():
                if pair[0] < i < pair[1] and s[i] not in pair[2]:
                    pair[2].append(s[i])

        return sum([len(pair[2]) for pair in pairs.values()])
# @lc code=end

