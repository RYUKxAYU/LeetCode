class Solution:
    def makeFancyString(self, s: str) -> str:
        res=s[0]
        l=s[0]
        count=1
        for i in range (1,len(s)):
            if s[i]!=l:
                l=s[i]
                count=0
            count+=1
            if count>2:
                continue
            res+=s[i]
        return res
            


            
        