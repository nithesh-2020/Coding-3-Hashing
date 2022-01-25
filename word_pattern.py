#leetcode problem: 205
#time complexity : O(N)
#space complexity : O(1) as the hashmap stores atmost 26 characters so we asymptotically we can consider as constant space

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w1=list(pattern)
        w2=s.split()
        if len(w1)!=len(w2):
            return False
        hm1={} #for keeping track of characters in w1
        hm2={} #for keeping track of the words in w2
        for x,y in zip(w1,w2):
            if x not in hm1:
                hm1[x]=y
            if y not in hm2:
                hm2[y]=x
            if x in hm1:
                if hm1[x]!=y:
                    return False
                
            if y in hm2:
                if hm2[y]!=x:
                    return False
        return True
        
