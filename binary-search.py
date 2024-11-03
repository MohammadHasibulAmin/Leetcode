#https://leetcode.com/problems/binary-search/

import numpy as np

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr = np.array(nums)
        length = arr.shape[0]

        low = 0
        high = length - 1

        while low <= high:
            mid = (high + low) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] < target:
                low = mid + 1
            
            else:
                high = mid-1

        return -1
        