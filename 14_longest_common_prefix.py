class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(0,len(strs)):
            while strs[i][:len(prefix)]!=prefix:
                prefix=prefix[:-1]
        if prefix:
            return prefix
        else:
            return ''
                