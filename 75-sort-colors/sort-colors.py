class Solution:
    def sortColors(self, nums: List[int]) -> None:
        s=0
        m=0
        e=len(nums)-1

        while m<=e:
            if nums[m]==0:
                nums[s],nums[m]=nums[m],nums[s]
                m+=1
                s+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[e]=nums[e],nums[m]
                e-=1
        return nums

        


        