from collections import defaultdict


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        print(self.count_char(s))
        print(self.count_char(t))

        return self.count_char(s) == self.count_char(t)

    def count_char(self, word: str):
        count = defaultdict(int)

        for char in word:
            count[char] += 1

        return count
