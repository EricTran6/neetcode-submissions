class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        if len(s) != len(t):
            return False
        for char in s:
            dicS[char] = dicS.get(char, 0) + 1
        for char in t:
            dicT[char] = dicT.get(char, 0) + 1
        return dicS == dicT
               
        

        