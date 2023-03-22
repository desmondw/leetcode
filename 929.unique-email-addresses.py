#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
import re
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = {}
        for email in emails:
            if (re.search("[^a-zA-Z.+]", email) is None): continue
            email = email.split('@')
            if (len(email) != 2): continue

            email[0] = email[0].split('+')[0].replace('.','')
            result['@'.join(email).lower()] = True

        return len(result)
# @lc code=end

