#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        # daysPerMonth = {
        #     '01': 31,
        #     '02': 29,
        #     '03': 31,
        #     '04': 30,
        #     '05': 31,
        #     '06': 30,
        #     '07': 31,
        #     '08': 31,
        #     '09': 30,
        #     '10': 31,
        #     '11': 30,
        #     '12': 31,
        # }

        daysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

        [year, month, day] = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)

        if month > 2 and year%4==0 and not (year%100==0 and year%400>0):
            day += 1

        day += sum(daysPerMonth[:month-1])

        return day

# @lc code=end

