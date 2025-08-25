import sys

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        current_sum = nums[0]
        global_max = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            global_max = max(global_max, current_sum)

        return global_max
