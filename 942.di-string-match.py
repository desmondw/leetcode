#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#

# @lc code=start
class Solution:
    # MINE WORKS - the DESCRIPTION has hidden criteria
    # def diStringMatch(self, s: str) -> List[int]:
    #     max = len(s)
    #     # max = s.count('D')
    #     stack = [0 if s[0]=='I' else max]
    #     for i in range(len(s)):
    #         # stack.append(stack[i-1] + (1 if s[i]=='I' else -1))
    #         if s[i] == 'I':
    #             stack.append(stack[i] + max)
    #         else:
    #             stack.append(stack[i] - 1)
    #     return stack

    def diStringMatch(self, S):
        i=0
        j=len(S)
        ans=[]

        for x in S:
            if x=='I':
                ans.append(i)
                i+=1
            else:
                ans.append(j)
                j-=1

        ans.append(j) #latest element
        return ans

# @lc code=end

