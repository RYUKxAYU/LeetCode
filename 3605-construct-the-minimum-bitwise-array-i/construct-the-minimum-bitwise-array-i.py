class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
#bitwise approach= observation= ans| ans+1 changes the lowest 0 bit of ans to 1...
#implication= nums[i] is essentially ans with one specific zero bit flipped to a one
#to find ans from nums[i] we will do a flip 1 bit back to 0-> which to flip is to flip the max(of bit)
#for edge case if num==2 we return -1
        for i in range(len(nums)):
            res=-1
            d=1
            while(nums[i]& d)!=0:
                res=nums[i]-d
                d<<=1
            nums[i]=res
        return nums

        