#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #字典
        n = len(nums)
        d = {}
        for x in range(n):
            a = target - nums[x]#减法好
            if nums[x] in d:
                return d[nums[x]],x
            else:
                d[a] = x
# @lc code=end

