class Solution:
    def longestPalindrome(self, s: str) -> str:
        st=0
        end=0
        for i in range(len(s)):
            l1=self.expands(s,i,i)
            l2=self.expands(s,i,i+1)

            max_len=max(l1,l2)
            if max_len>end-st:
                st=i-(max_len -1)//2
                end=i+ max_len//2
        return s[st:end+1]

    
    def expands(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return r-l-1

        
        