class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in dict:
                return dict[complement], i+1
            dict[numbers[i]]=i+1