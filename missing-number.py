#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max = 0
        min = 0
        list_1 = []
        for i in nums:
            if i >= max: max = i

        for i in range(min,max):
            list_1.append(i)

        list_1.append(len(nums))

        for i in range(len(list_1)):
            if list_1[i] not in nums:
                return list_1[i]