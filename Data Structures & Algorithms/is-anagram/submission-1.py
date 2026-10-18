class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seenS = {}
        seenT = {}
        for char in s:
            seenS[char] = seenS.get(char, 0) + 1
        for char in t:
            seenT[char] = seenT.get(char, 0) + 1
        return seenS == seenT