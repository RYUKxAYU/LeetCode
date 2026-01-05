# class Solution:
#     def sumFourDivisors(self, nums: list[int]) -> int:
#         res = 0
#         for n in nums:
#             val = self.sumOne(n)
#             if val != -1:
#                 res += val
#         return res

#     def sumOne(self, n: int) -> int:
#         p = round(n ** (1/3))
#         if p ** 3 == n and self.isPrime(p):
#             return 1 + p + p*p + p*p*p

#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 a, b = i, n // i
#                 if a != b and self.isPrime(a) and self.isPrime(b):
#                     return 1 + a + b + n
#                 return -1
#         return -1

#     def isPrime(self, x: int) -> bool:
#         if x < 2:
#             return False
#         for i in range(2, int(x ** 0.5) + 1):
#             if x % i == 0:
#                 return False
#         return True
                    


#         # for i in range(len(nums)):
#         #     # You only need to loop to the square root of a number to find its divisors.
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divisors = []
            # Find all divisors up to sqrt(n)
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:  # Avoid duplicate for perfect squares
                        divisors.append(n // i)
            
            # If exactly 4 divisors, sum them
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total          