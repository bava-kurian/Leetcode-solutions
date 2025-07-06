#recursive solution


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        def helper(index1,index2):
            if index1>m-1 and index2>n-1:
                return 0
            if index1>m-1:
                return n-index2
            if index2>n-1:
                return m-index1
            
            if word1[index1]==word2[index2]:
                return helper(index1+1,index2+1)
            
            insert=1+helper(index1,index2+1)
            delete=1+helper(index1+1,index2)
            replace=1+helper(index1+1,index2+1)

            return min(insert,delete,replace)
        return helper(0,0)


# Time complexity: O(3^(m+n)) where m is the length of word1 and n is the length of word2
# Space complexity: O(m+n) for the recursion stack

#Memoization solution

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        @lru_cache(None)
        def helper(index1,index2):
            if index1>m-1 and index2>n-1:
                return 0
            if index1>m-1:
                return n-index2
            if index2>n-1:
                return m-index1
            
            if word1[index1]==word2[index2]:
                return helper(index1+1,index2+1)
            
            insert=1+helper(index1,index2+1)
            delete=1+helper(index1+1,index2)
            replace=1+helper(index1+1,index2+1)

            return min(insert,delete,replace)
        return helper(0,0)
# Time complexity: O(m*n) where m is the length of word1 and n is the length of word2
# Space complexity: O(m*n) for the memoization cache