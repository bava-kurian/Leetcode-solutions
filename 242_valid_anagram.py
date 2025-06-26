class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash={}
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        print(hash)
        if len(s)!=len(t):
            return False
        for i in t:
            if i not in hash:
                return False
            if t.count(i) != hash[i]:
                return False
        return True
    
    #very simplae and efficient solution
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
