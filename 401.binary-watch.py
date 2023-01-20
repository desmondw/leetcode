#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
import itertools
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        n = turnedOn
        hourOptions = min(3, n)
        times = []

        for h in range(hourOptions+1):
            m = n - h
            if m <= 5:
                times += self.getValidTimes(h, m)

        return times

    def getValidTimes(self, h, m):
        hours = self.getValidHours(h)
        mins = self.getValidMins(m)

        times = map(lambda h: [f'{h}:{m}' for m in mins], hours)
        times = [x for hoursList in times for x in hoursList]

        return times

    def getValidHours(self, h):
        if h == 0: return ['0']
        arrs = self.getTruncArrsSumLimit(h, [8,4,2,1], 12)
        return [str(m) for m in arrs]

    def getValidMins(self, m):
        if m == 0: return ['00']
        arrs = self.getTruncArrsSumLimit(m, [32, 16, 8, 4, 2, 1], 60)
        return [f'{m:0>2}' for m in arrs]

    def getTruncArrsSumLimit(self, n, arr, limit):
        combos = list(itertools.combinations(arr, n))
        result = [x for c in combos if (x:=sum(c)) < limit]
        return result

# @lc code=end

