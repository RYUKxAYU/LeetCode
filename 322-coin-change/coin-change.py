class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=float('inf')
        dp=[INF]*(amount+1)
        dp[0]=0

        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0 and dp[a-c]!=INF:
                    dp[a]=min(dp[a],dp[a-c]+1)

        return dp[amount] if dp[amount]!=INF else -1       