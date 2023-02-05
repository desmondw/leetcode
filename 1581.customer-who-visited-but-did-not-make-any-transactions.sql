--
-- @lc app=leetcode id=1581 lang=mysql
--
-- [1581] Customer Who Visited but Did Not Make Any Transactions
--

-- @lc code=start
# Write your MySQL query statement below

select customer_id, count(*) as count_no_trans
from Visits left join Transactions on Visits.visit_id = Transactions.visit_id
where Transactions.visit_id is null
group by customer_id

-- @lc code=end

