class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        # dp[i][j] = max dot product using nums1[0:i] and nums2[0:j]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        # Base case: initialize with first product
        dp[1][1] = nums1[0] * nums2[0]
        
        # Fill first row
        for j in range(2, m + 1):
            dp[1][j] = max(dp[1][j-1], nums1[0] * nums2[j-1])
        
        # Fill first column
        for i in range(2, n + 1):
            dp[i][1] = max(dp[i-1][1], nums1[i-1] * nums2[0])
        
        # Fill rest of table
        for i in range(2, n + 1):
            for j in range(2, m + 1):
                product = nums1[i-1] * nums2[j-1]
                
                # Option 1: Start fresh with this product
                # Option 2: Extend from previous best (including this product)
                # Option 3: Skip current in nums1 → dp[i-1][j]
                # Option 4: Skip current in nums2 → dp[i][j-1]
                
                dp[i][j] = max(
                    product,
                    dp[i-1][j-1] + product,
                    dp[i-1][j],
                    dp[i][j-1]
                )
        
        return dp[n][m]