# Pattern: Sliding Window
# Difficulty: Medium
# Common Mistake: Not shrinking the left pointer when a duplicate is hit


#Problem: Given a string s, return the length of the longest substring without repeating characters.

# def lengthOfLongestSubstring(s):
#     max_len = 0
#     left = 0
#     char_set = set()

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left +=1 

        
#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)

#     return max_len


# print(lengthOfLongestSubstring("abcabcbb")) # Had 1 hint to complete.
