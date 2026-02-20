class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick={}
        for i,num in enumerate(nums):
            comple=target-num
            if comple in dick:
                return[dick[comple],i]
            dick[num]=i
        return []
         