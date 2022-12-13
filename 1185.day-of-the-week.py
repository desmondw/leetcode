#
# @lc app=leetcode id=1185 lang=python3
#
# [1185] Day of the Week
#

# @lc code=start
import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = datetime.datetime(year, month, day)
        return date.strftime("%A")
# @lc code=end

