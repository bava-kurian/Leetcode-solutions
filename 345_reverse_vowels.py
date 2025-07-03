#two pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        v=["a","e","i","o","u","A","E","I","O","U"]
        i,j=0,len(s)-1
        s_list=list(s)
        while i<j:
            if s_list[i] not in v:
                i+=1
            elif s_list[j] not in v:
                j-=1
            else:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i,j=i+1,j-1
        s="".join(s_list)
        return s
        
        


            
        