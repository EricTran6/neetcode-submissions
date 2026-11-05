class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words:
            cur_count = Counter(word)
            for char in count:
                count[char] = min(count[char], cur_count[char])

        result = []
        for c in count:
            for i in range(count[c]):
                result.append(c)
        return result
