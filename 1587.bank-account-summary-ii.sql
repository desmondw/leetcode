--
-- @lc app=leetcode id=1587 lang=mysql
--
-- [1587] Bank Account Summary II
--

-- @lc code=start
# Write your MySQL query statement below

select u.name, sum(t.amount) as balance
from Users as u right join Transactions as t on u.account = t.account
group by t.account
having sum(t.amount) > 10000

-- @lc code=end

