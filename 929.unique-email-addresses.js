/*
 * @lc app=leetcode id=929 lang=javascript
 *
 * [929] Unique Email Addresses
 */

// @lc code=start
/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
  let validEmails = {}
  emails.forEach(email=>{
    if (/[^a-z.+@]/.test(email)) return
    if ((email = email.split('@')).length > 2) return

    email[0] = email[0].split('+')[0]
    email = email[0].split('.').join('') + '@' + email[1]
    validEmails[email] = true
  })
  return Object.keys(validEmails).length
};
// @lc code=end

