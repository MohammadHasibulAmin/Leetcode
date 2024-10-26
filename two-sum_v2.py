#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_saver = []
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    idx_saver.append(i)
                    idx_saver.append(j)

        return idx_saver