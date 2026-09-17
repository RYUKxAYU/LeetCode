class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged=[]
        i,j=0,0
        len1, len2=len(nums1),len(nums2)
        while i <len1 and j<len2:
            if nums1[i]<=nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        total_len=len(merged)
        mid=total_len//2

        if total_len % 2==1:
            median=float(merged[mid])
        else:
            median=((merged[mid-1]+merged[mid])/2.0)
        
        # return f"{median:.5f}"
        return median
        # print(f"{median:.5f}")