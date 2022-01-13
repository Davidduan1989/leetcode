#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子数组和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = -10000
        max_current = 0
        for i in range(0,len(arr)):
            if max_current + arr[i] >= arr[i]:
                max_current = max_current+ arr[i]
            else:
                max_current = arr[i]
        if max_so_far < max_current:
            max_so_far = max_current
        return max_so_far
# @lc code=end

