class Solution:
    def countOdds(self, low: int, high: int) -> int:
        mid = (high - low) // 2

        # if either R or L is odd
        if (high % 2 != 0 or low % 2 != 0):
            mid += 1

        return mid