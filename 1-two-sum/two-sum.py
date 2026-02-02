class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap={}
        n=len(nums)
        for i in range(n):
            nMap[nums[i]]=i
        
        for i in range(n):
            complement=target-nums[i]
            if complement in nMap and nMap[complement]!=i:
                return[i,nMap[complement]]
        return[]

        # for i in range len(nums):
        #     comp=target-nums[i] 
        #     if comp not in num:
        #         num.append(nums[i])
        #         return 
            


        