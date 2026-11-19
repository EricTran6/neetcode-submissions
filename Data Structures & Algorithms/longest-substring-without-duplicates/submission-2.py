class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 0
        l = 0
        subset = set()
        for r in range(len(s)):
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            subset.add(s[r])
            longest = max(longest, r - l + 1)
        return longest