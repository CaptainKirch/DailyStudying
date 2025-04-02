# Problem Statement:
# Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If no such window exists, return an empty string "".

# from collections import Counter

# def minWindow(s, t):
#     if len(t) > len(s):
#         return ""
    
#     target_count = Counter(t)
#     window_count = {}

#     have  = 0
#     need = len(target_count)

#     res = [-1,-1]
#     res_len = float('inf')
#     left = 0


#     for right in range(len(s)):
#         window_count[s[right]] = window_count.get(s[right], 0) + 1

#         if s[right] in target_count and window_count[s[right]] == target_count[s[right]]:
#             have += 1


#         while have == need:
#             if (right - left + 1) < res_len:
#                 res = [left, right]
#                 res_len = right - left + 1


#             window_count[s[left]] -= 1
#             if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
#                 have -= 1

#             left += 1

#     if res_len == float('inf'):
#         return ""

#     return s[res[0] : res[1] + 1]

        



















# print(minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
# print(minWindow("a", "a"))                # "a"
# print(minWindow("a", "aa"))               # ""
