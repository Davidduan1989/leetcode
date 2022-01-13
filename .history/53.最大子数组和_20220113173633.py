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
        for i in range(0,len(nums)):
            if max_current + nums[i] >= nums[i]:
                max_current = max_current+ nums[i]
            else:
                max_current = nums[i]
        if max_so_far < max_current:
            max_so_far = max_current
        return max_so_far
# @lc code=end

