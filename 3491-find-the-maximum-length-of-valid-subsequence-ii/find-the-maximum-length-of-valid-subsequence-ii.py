class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        max_len=2
        for targ_mod in range(k):
            rem_dp=[0]*k

            for num in nums:
                num_mod=num%k
                req_mod=(targ_mod-num_mod+k)%k
                rem_dp[num_mod]= rem_dp[req_mod]+1

            max_len=max(max_len,max(rem_dp))
        return max_len