class Solution:
    def isHappy(self, n: int) -> bool:
        def gnn(n):
            output=0
            while n:
                digit=n%10
                output+=digit**2
                n=n//10
            return output

        slow=gnn(n)
        fast=gnn(gnn(n))

        while slow !=fast:
            if fast ==1: return True
            slow=gnn(slow)
            fast=gnn(gnn(fast))
        
        return fast==1
        