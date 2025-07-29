import functools
import operator
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_overall_or = 0 # Calculated first
        for num in nums:
            max_overall_or |= num

        dp_size = 1 << max_overall_or.bit_length() if max_overall_or > 0 else 1 # Dynamic size
        dp = [0] * dp_size

        dp[0] = 1

        max_current_or = 0 # Similar to original max_oR

        for num in nums:
            for i in range(max_current_or, -1, -1):
                if dp[i] > 0: # Added optimization
                    dp[i | num] += dp[i]
            max_current_or |= num

        return dp[max_overall_or]