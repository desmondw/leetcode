/*
 * @lc app=leetcode id=278 lang=javascript
 *
 * [278] First Bad Version
 */

// @lc code=start
/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    let check = function(high, low=0) {
        if (!isBadVersion(high) && isBadVersion(high+1)) return high+1
        if (!isBadVersion(low) && isBadVersion(low+1)) return low+1
        let mid = low + ~~((high-low)/2)
        if (isBadVersion(mid)) return check(mid, low)
        else return check(high, mid)
    }
    return check
};
// @lc code=end

