# leetcode problem number : 525
# time complexity : O(N)
# space complexity: O(N)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        maxLength = 0
        
        d = {0:-1}
        
        runningSum = 0
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                runningSum += -1
            
            else:
                runningSum += 1
            
            if runningSum in d:
                maxLength = max(maxLength,i-d[runningSum])
            
            else:
                d[runningSum] = i
            
        return maxLength
