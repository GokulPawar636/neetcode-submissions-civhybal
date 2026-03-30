class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        li1 = list(s)

        for j in t:
            if j in li1:
                li1.remove(j)
            else:
                return False
        return True