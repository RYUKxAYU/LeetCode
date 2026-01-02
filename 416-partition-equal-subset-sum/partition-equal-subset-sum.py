class Solution(object):
    def canPartition(self, nums):
        s=sum(nums)
        if s%2!=0:
            return False
        t=s//2
        n=len(nums)
        dp=[False]*(t+1)
        dp[0]=True
        for i,num in enumerate(nums):
            for j in range(t,num-1,-1):
                dp[j]=dp[j] or dp[j-num]
        return dp[t]
