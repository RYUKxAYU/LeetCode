class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=0
        S = self.clean_sentence(s)
        end=len(S)-1
        if not S:
            return True
        while st<end:
            if S[st]!=S[end]:
                return False
            st+=1
            end-=1
        return True
    def clean_sentence(self,sentance: str) -> str:
        return ''.join(filter(str.isalnum, sentance)).lower()
        