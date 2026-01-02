class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Create an empty set to track seen elements
        seen=set()
        # Iterate through each element in nums:
        for x in nums:
            # Check if the element is already in the set
            if x in seen:
                return x
            # If not seen before, add it to the set    
            seen.add(x)
        