class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for k, v in enumerate(nums):
            rest = target - v
            
            if rest in map:
                return [map[rest], k]
            
            map[v] = k
