#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        sorted_nums = sorted(nums)
    
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True
            
        return False