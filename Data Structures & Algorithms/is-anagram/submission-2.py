class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = sorted(s)
        tList = sorted(t)
        return sList == tList