class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict=defaultdict(int)
        balloon='balloon'
        i=0
        while(i<len(text)):
            if text[i] in balloon:
                dict[text[i]]+=1
            i+=1
        return(min(dict['b'],dict['a'],dict['l']//2,dict['o']//2,dict['n']))