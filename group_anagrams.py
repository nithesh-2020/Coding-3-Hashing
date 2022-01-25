# leetcode problem : 49
# time complexity : O(N*k) => k=len(word)
# space complexity : O(N)  

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def primeProduct(char):
            
            primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
            
            product = 1
            
            for c in char:
                
                product*=primes[ord(c)-ord('a')]
            
            return product
                
            
        
        d={}  #hashmap use to store the list of anagrams as value and primeproduct as key
        
        for char in strs:
            
            key = primeProduct(char) # it returns the prime product value for each char
            
            if key not in d:
                d[key] = [] #make a list for each key
            
            d[key].append(char) 
            
        ans=[]
        
        for key in d.keys():
            
            ans.append(d[key])
        
        return ans
