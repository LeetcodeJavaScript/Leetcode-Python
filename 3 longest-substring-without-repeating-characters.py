class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        map = {}
        res = 0
        
        for i, ch in enumerate(s):
            left = map[ch] + 1 if ch in map and map[ch] >= left else left
            map[ch] = i
            res = max(res, i - left + 1)
            
        return res
