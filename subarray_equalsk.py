# leetcode problem number : 560
# time complexity : O(N)
# space complexity : O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = {0:1} 
        
        cnt = 0
        
        runningSum = 0
        
        for i in range(len(nums)):
            
            runningSum += nums[i]
            
            if runningSum - k in d:
                cnt += d[runningSum-k]
            
            if runningSum not in d:
                d[runningSum] = 1
            
            else:
                d[runningSum]+=1
            
        return cnt
