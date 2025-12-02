class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts={}
        n=len(nums)
        thresold=n//2
        for i in nums:
            counts[i]=counts.get(i,0)+1
        for elements, count in counts.items():
            if count>thresold:
                return elements
        return -1 