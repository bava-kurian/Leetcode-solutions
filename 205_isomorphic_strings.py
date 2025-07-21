class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        for i in range(len(s)):
            if s[i] not in hash1:
                hash1[s[i]] =t[i] 
            else:
                if t[i]!=hash1[s[i]]:
                    return False
            if t[i] not in hash2:
                hash2[t[i]] =s[i] 
            else:
                if s[i]!=hash2[t[i]]:
                    return False
        return True