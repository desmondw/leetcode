--
-- @lc app=leetcode id=1741 lang=mysql
--
-- [1741] Find Total Time Spent by Each Employee
--

-- @lc code=start
# Write your MySQL query statement below

select event_day as day,
  emp_id,
  (sum(out_time) - sum(in_time)) as total_time
  from Employees e
  group by emp_id, event_day

-- @lc code=end

