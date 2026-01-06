class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early length check
        if len(s) != len(t):
            return False
        
        # Count frequency of characters in s
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        
        # Subtract frequency for each character in t
        for c in t:
            if c not in char_count:
                return False
            char_count[c] -= 1
            if char_count[c] == 0:
                del char_count[c]
        
        # If no characters left, it's an anagram
        return True