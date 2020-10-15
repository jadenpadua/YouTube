class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentMax = nums[0]
        globalMax = nums[0]
        
        for num in nums[1:]:
            currentMax = max(currentMax + num, num)
            globalMax = max(globalMax, currentMax)
            
        return globalMax
