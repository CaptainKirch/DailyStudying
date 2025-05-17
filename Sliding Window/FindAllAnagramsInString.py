# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.


# from collections import Counter

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> list[int]:
#         res = []
#         s_count = Counter(s)
#         p_count = Counter()
#         left = 0

    
#         for right in range(len(s)):
#             s_count[s[right]] += 1
            
#             if right - left + 1 > len(p):
#                 s_count[s[left]] -= 1
#                 if s_count[s[left]] == 0:
#                     del s_count[s[left]]

#                 left += 1


#             if s_count == p_count:
#                 res.append(left)

#         return res
