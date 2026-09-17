class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        res=[]
        cycle=2* numRows-2
        n=len(s)
        for r in range(numRows):
            for i in range(r,n,cycle):
                res.append(s[i])
                diag_idx=i+cycle-2*r
                if 0<r<numRows -1 and diag_idx<n:
                    res.append(s[diag_idx])
        
        return "".join(res)