class Solution:
    def maxArea(self, height: List[int]) -> int:
        st,end,max_area=0,len(height)-1,0
        while st<end:
            max_area=max(max_area,(end-st)*min(height[st],height[end]))
            if height[st]<height[end]:
                st+=1
            else:
                end-=1
        return max_area
        