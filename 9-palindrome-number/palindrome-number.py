class Solution:
    def isPalindrome(self, x: int) -> bool:
        st=0
        s=str(x)
        end=len(s)-1
        if len(s)<1:
            return ""
        while st<end:
            if s[st]!=s[end]:
                return False
            st+=1
            end-=1
        return True
            
        