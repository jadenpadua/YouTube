class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prevSums = {0:1}
        runningSum = 0
        count = 0
        
        for i in range(len(nums)):
            runningSum += nums[i]
            prevSumToFind = runningSum - k
            
            if prevSumToFind in prevSums:
                count += prevSums[prevSumToFind]
            
            prevSums[runningSum] = prevSums.get(runningSum, 0) + 1
        
        return count
