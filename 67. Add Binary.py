class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x,y=int(a,2),int(b,2)

        while y:
            add=x^y
            carry=(x&y)<<1
            x,y=add,carry
        return bin(x)[2:]