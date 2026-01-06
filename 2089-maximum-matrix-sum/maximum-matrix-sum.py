class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        ts = 0
        neg = 0
        minAbs = float('inf')

        for row in matrix:
            for v in row:
                if v < 0:
                    neg += 1
                av = abs(v)
                ts += av
                minAbs = min(minAbs, av)

        return ts if neg % 2 == 0 else ts - 2 * minAbs