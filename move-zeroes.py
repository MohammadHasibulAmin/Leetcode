#https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        """Do not return anything, modify nums in-place instead."""

        length = len(nums)

        j = -1
        for i in range(length):
            if nums[i] == 0:
                j = i
                break

        if j == -1: return nums

        for i in range(j+1, length):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1