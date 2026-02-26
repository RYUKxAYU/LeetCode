class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        duplicate = 0
        for bit in range(32):
            mask = (1 << bit)
            count_nums = 0
            count_range = 0
            
            for i in range(len(nums)):
                # Count bits in the actual array
                if nums[i] & mask:
                    count_nums += 1
                
                # Count bits in the range 1 to n
                if i > 0 and (i & mask):
                    count_range += 1
            
            # If the bit is more frequent in the array, 
            # it belongs to our duplicate number.
            if count_nums > count_range:
                duplicate |= mask
                
        return duplicate