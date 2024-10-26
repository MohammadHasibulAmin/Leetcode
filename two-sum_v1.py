#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        import numpy as np
        arr1 = np.array(nums)
        idx1 = 0
        idx2 = 0
        list1 = []
        for i in range(arr1.size):
            for j in range(i+1,arr1.size):
                if arr1[i] + arr1[j] == target:
                    idx1 = i
                    idx2 = j
        list1 += idx1,idx2
        return list1