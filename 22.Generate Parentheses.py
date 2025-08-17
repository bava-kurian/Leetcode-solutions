class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(open,close,s):
            if len(s)==2*n:
                ans.append(s)
                return 
            if open <n:
                backtrack(open+1,close,s+'(')
            if close < open:
                backtrack(open,close+1,s+')')
        backtrack(0,0,"")
        return ans
                
