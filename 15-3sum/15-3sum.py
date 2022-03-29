class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if (all(num == 0 for num in nums)):
            return [[0, 0, 0]]
        size = len(nums) 
        found = {}
        nums = sorted(nums)
        for index, value in enumerate(nums):
            left = index + 1
            right = size - 1
            while left < right:
                total = value + nums[left] + nums[right]
                if total == 0:
                    current = (value, nums[left], nums[right])
                    if current not in found:
                        found[current] = True
                    right = right - 1
                elif total < 0:
                    left = left + 1
                else:
                    right = right - 1
        return list(found.keys())
