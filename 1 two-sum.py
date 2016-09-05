class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        
        for i, v in enumerate(nums):
            rest = target - v
            
            if rest in map:
                return [map[rest], i]
                
            map[v] = i
