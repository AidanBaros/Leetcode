class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j, mun in enumerate(nums):
                if ((num + mun) == target) and i != j:
                    return [i,j]
        