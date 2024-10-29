class Solution:
    def check(self, nums: List[int]) -> bool:
        rotation_count = 0

        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                rotation_count += 1

        return True if rotation_count <= 1 else False