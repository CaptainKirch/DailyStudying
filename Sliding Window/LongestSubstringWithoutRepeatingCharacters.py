# Pattern: Sliding Window
# Difficulty: Medium
# Common Mistake: Not shrinking the left pointer when a duplicate is hit


#Problem: Given a string s, return the length of the longest substring without repeating characters.

# def LongestSubstring(s):
#     char_set = set() # We define a set so that no duplicates can be stored in this structure.
#     max_len = 0 # We define the variable max_len as we need to find the longest substring length.
#     left = 0 # We define left as we need to use it for the left pointer for the sliding window.

#     for right in range(len(s)): # We create a for loop over the entire range length of the string.
#         while s[right] in char_set: #As long as the current character is in the set we continue to shrink left.
#             char_set.remove(s[left]) # This is removing the character from the sliding window of the left pointer.
#             left += 1 # Shrinks the left pointer adding 1.

#         char_set.add(s[right]) # When sliding window moves this adds next character to the set for the right pointer.
#         max_len = max(max_len, right - left + 1) # This defines the new max length of the no duplicates found set.

#     return max_len 


# More Drilling Attemps Below ---------------------------------------------


# def LongestSubstring(s):
#     char_set = set()
#     max_len = 0
#     left = 0

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1

#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)

#     return max_len

# def LongestSubstring(s):
#     char_set = set()
#     max_len = 0
#     left = 0


#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1

#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)

#     return max_len