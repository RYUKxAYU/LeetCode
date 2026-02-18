class Solution:
    def maxArea(self, height: List[int]) -> int:
        st,end=0,len(height)-1
        maxx_res=0
        while st<end:
            res=end-st
            curr_res=min(height[st],height[end])*res
            
            maxx_res=max(maxx_res,curr_res)
            
            if height[st]<height[end]:
                st+=1
            else:
                end-=1        
        return maxx_res
            

        