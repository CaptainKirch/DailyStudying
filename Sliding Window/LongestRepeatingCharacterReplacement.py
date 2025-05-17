# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing at most k replacements.

# from collections import defaultdict

# def characterReplacement(s, k):
#     max_len = 0
#     max_count = 0
#     left = 0
#     count = defaultdict(int)

#     for right in range(len(s)):
#         count[s[right]] += 1
#         max_count =  max(max_count, count[s[right]])

#         window_len = right - left + 1
#         if window_len - max_count > k:
#             count[s[left]] -= 1
#             left += 1

#     max_len = max(max_len, right - left + 1)

#     return max_len


# print(characterReplacement("ABAB", 2)) # Had 2 Hints To Help Complete

# from collections import defaultdict

# def characterReplacement(s, k):
#     count = defaultdict(int)
#     max_len = 0
#     left = 0
#     max_count = 0


#     for right in range(len(s)):
#         count[s[right]] += 1
#         max_count = max(max_count, count[s[right]])


#         window_len = right - left + 1
#         if window_len - max_count > k:
#             count[s[left]] -= 1
#             left += 1


#         max_len = max(max_len, right - left + 1)


#     return max_len

# print(characterReplacement("AABABBA", 1))
# # 4
