#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
import re
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if not re.match('[A-Za-z]',s[i]):
                i+=1
                continue
            elif not re.match('[A-Za-z]',s[j]):
                j-=1
                continue
            swap = s[i]
            s[i] = s[j]
            s[j] = swap
            i+=1
            j-=1
        return ''.join(s)


# @lc code=end

