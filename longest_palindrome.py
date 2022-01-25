# leetcode problem number : 409
# time complexity : O(N)
# space complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        hashSet = set()
        
        res = 0
        
        for i in range(len(s)):
            
            if s[i] in hashSet:
                
                res += 2
                hashSet.remove(s[i])
                
            else:
                
                hashSet.add(s[i])
        
        if not hashSet:
            return res
        return res+1
