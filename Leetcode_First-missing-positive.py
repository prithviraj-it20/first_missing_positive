class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        i = 1
        for num in nums:
            if num == i:
                i += 1
            elif num > 0:
                return i
        return i

        
                    
        
