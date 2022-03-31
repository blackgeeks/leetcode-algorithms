class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]

        #if len(nums)==3:
        #    return closest

        for i in range(len(nums)):
            if i!=len(nums)-1:
                temp = nums[:i] + nums[i+1:]
            else:
                temp = nums[:len(nums)-1]

            temp = sorted(temp)

            l, r = 0, len(temp) -1 
            t = target - nums[i]

            while(l < r):
                if abs(temp[l] + temp[r] + nums[i] - target) < abs(closest - target):
                        closest = temp[l] + temp[r] + nums[i]

                if temp[l] + temp[r] == t:

                    return target
                elif temp[l] + temp[r] > t:
                    r = r - 1
                else:
                    l = l + 1

        return closest