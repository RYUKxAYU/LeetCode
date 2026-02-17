class Solution:
    def isPalindrome(self, s:str)->bool:
        st,end=0,len(s)-1
        while st<end:
            while st<end and not s[st].isalnum():
                st+=1
            while st<end and not s[end].isalnum():
                end-=1
            if s[st].lower()!=s[end].lower():
                return False
            
            st+=1
            end-=1
        return True