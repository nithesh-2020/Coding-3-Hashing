#leetcode problem: 205
#time complexity : O(N)
#space complexity : O(1) as the hashmap stores atmost 26 characters so we asymptotically we can consider as constant space

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hm1 = {}
        hm2 = {}
        
        for x,y in zip(s,t):
            
            if x not in hm1:
                hm1[x] = y
            
            else:
                if hm1[x] != y:
                    return False
            if y not in hm2:
                hm2[y] = x
            
            else:
                if hm2[y] != x:
                    return False
        
        return True
