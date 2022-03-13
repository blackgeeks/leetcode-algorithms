class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = nums.count(0)
        for i in range(zero_num):
            nums.remove(0)
            nums.append(0)