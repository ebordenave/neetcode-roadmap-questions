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
        
# Optimized solution -> one hashmap
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count_s = defaultdict(int)

#         for c in s:
#             count_s[c] += 1

#         for c in t:
#             if c not in count_s:
#                 return False

#             count_s[c] -= 1
            
#             if count_s[c] < 0:
#                 return False

#         return True
    
