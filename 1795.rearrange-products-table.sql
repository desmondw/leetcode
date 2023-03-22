--
-- @lc app=leetcode id=1795 lang=mysql
--
-- [1795] Rearrange Products Table
--

-- @lc code=start
# Write your MySQL query statement below

select * from (
  select product_id, 'store1' store, store1 price from Products union all
  select product_id, 'store2' store, store2 price from Products union all
  select product_id, 'store3' store, store3 price from Products
) as fu
where fu.price is not null
order by fu.product_id

-- @lc code=end

