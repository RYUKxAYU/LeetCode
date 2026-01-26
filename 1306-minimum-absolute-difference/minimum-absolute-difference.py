class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n=len(arr)
        min_diff=2e6+1
        res=[]
        for i in range(1,n):
            diff=arr[i]-arr[i-1]
            if diff<min_diff:
                min_diff=diff
                res=[[arr[i-1],arr[i]]]
            elif diff==min_diff:
                res.append([arr[i-1],arr[i]])
        return res