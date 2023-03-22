#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        pMax = max(salary[0], salary[1])
        pMin = min(salary[0], salary[1])
        sum = 0

        for pay in salary[2:]:
            if pay < pMin:
                sum += pMin
                pMin = pay
            elif pay > pMax:
                sum += pMax
                pMax = pay
            else:
                sum += pay

        return sum / (len(salary)-2)

# @lc code=end

