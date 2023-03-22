--
-- @lc app=leetcode id=1757 lang=mysql
--
-- [1757] Recyclable and Low Fat Products
--

-- @lc code=start
# Write your MySQL query statement below
select p.product_id from Products as p where p.low_fats = 'Y' and p.recyclable = 'Y'
-- @lc code=end

