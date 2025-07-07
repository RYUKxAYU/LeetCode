class Solution:
    def rec(self, open,close,CurrString,res):
        if open==0 and close==0:
            res.append(CurrString)
            return
        if open>0:
            self.rec(open-1,close,CurrString+'(',res)
        if close>open:
            self.rec(open,close-1,CurrString+')',res)
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        self.rec(n,n,"",ans)
        return ans


        