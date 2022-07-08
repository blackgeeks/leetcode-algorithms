class Solution:
    def newArray(self,array):
        arr = [0] * (len(array) -1 )
        for num in range(0,len(array)-1):
            arr[num] = (array[num] + array[num + 1]) %10
        return arr

    def triangularSum(self, nums: List[int]) -> int:
        dic = {}
        dic[0] = nums
        
        
        for i in range(1, len(nums)):
            dic[i] = self.newArray(dic[i - 1])

        return dic[len(nums) -1 ][0]
