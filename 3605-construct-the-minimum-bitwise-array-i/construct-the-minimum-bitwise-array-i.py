class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            real=num
            candi=-1
            for j in range(1,real):
                if(j|(j+1))==real:
                    candi=j
                    break
            res.append(candi)
        return res
        