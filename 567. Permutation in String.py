class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        n, m = len(s2), len(s1)
        if m > n:
            return False
        
        count1 = Counter(s1)              # frequency count of s1
        window = Counter(s2[:m])          # first window in s2
        
        if window == count1:
            return True
        
        for i in range(m, n):
            # Add new char in the window
            window[s2[i]] += 1
            # Remove old char from the left
            window[s2[i-m]] -= 1
            if window[s2[i-m]] == 0:      # clean up to keep dicts equal
                del window[s2[i-m]]
            
            if window == count1:
                return True
        
        return False
