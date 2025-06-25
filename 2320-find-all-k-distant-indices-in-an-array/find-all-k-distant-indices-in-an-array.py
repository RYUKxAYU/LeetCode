class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res_index=[]
        len_num=len(nums)

        for i in range(len_num):
            for j in range(len_num):
                if abs(i-j)<=k and nums[j]==key:
                    res_index.append(i)
                    break
        return res_index