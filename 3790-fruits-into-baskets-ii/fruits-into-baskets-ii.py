class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        unplaced=0
        used_baskets=[False]*n

        for i in range(n):
            fruits_quantity=fruits[i]
            placed=False

            for j in range(n):
                if not used_baskets[j] and baskets[j]>= fruits_quantity:
                    used_baskets[j]= True
                    placed = True
                    break
            if not placed:
                unplaced= unplaced+1

        return unplaced