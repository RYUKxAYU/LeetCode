class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j=0
        for n in nums:
            if j<0:
                return False
            elif n>j:
                j=n
            j-=1
        return True 
        