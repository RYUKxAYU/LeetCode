class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s=list(s)
        res=0
        while s:
            i=s.index(s[-1])
            if i==len(s)-1:
                res+=(i//2)
            else:
                res+=i
                s.pop(i)
            s.pop()
        return res

#         st=0
#         end=len(s)-1
#         while st<end:
#             if s[st]==s[end]:
#                 st+=1
#                 end-1
#             else:
#                 if s[st+1]==s[end]:
#                     s[st],s[st+1]=s[st+1],s[st]
#                 else:
#         # while left<right:    
#         # clear="".join(char.lower() for char in s if char.isalnum())
#         # if clear==clear[::-1]:
#         #     count+=1
        
#         # return count
#         """
#         s = "ievbkcweviubcqooqebc"
# left, right = 0, len(s) - 1

# # Example: Checking if s is a palindrome
# is_palindrome = True
# while left < right:
#     if s[left] != s[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1

# print(f"Is palindrome: {is_palindrome}")
#         """

        