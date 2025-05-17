# # Problem Statement:
# # Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# # If no such window exists, return an empty string "".

# from collections import Counter # We are importing the Counter from collections as we need to count the characters and make sure they match the second string.

# def minWindow(s, t): 
#     if len(t) > len(s): # We are acommadating for the edge case in the beginning so that if the window is none exsistant we are gonna reply with "".
#         return ""
    
#     target_count = Counter(t) # We are definfing target count as counting the characters inside the strin go "t"
#     window_count = {} # We need an empty hash map to compare the the desired characters with the current ones.

#     have  = 0 #We define this to keep track of what character we have already. When expanding the window.
#     need = len(target_count)  # We are tracking what characters we need from the target_count which has been Counted as shown above.

#     res = [-1,-1] #This is a starting res at the beginning and end of the indicies.
#     res_len = float('inf') # This is allowing us to have infinity for the len of the res.
#     left = 0 # Sliding window left pointer.


#     for right in range(len(s)): # For loop that is looping over the string of "s", and under this we are gonna be adding each letter of the string into the hashmap and tracking its frequency and type.
#         window_count[s[right]] = window_count.get(s[right], 0) + 1

#         if s[right] in target_count and window_count[s[right]] == target_count[s[right]]:
#             have += 1 #This if statement is if the character is already in target_count and the frequency of the char is identical to target count frquency, we are gonna move the "have" up one as counting how many chars we have as we have found one.

#         while have == need: # This is a while loop and under if the current index of the window is less than the length of the re_len we are gonna be .... idk...
#             if (right - left + 1) < res_len:
#                 res = [left, right]
#                 res_len = right - left + 1


#             window_count[s[left]] -= 1 #Moving the sliding window and removing the left pointer element.
#             if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
#                 have -= 1 # Same as above but its for the left pointer.

#             left += 1 

#     if res_len == float('inf'):
#         return "" # This is another edge case situation, so that even after the entire sliding window we retunr the ""

#     return s[res[0] : res[1] + 1] # We are returning,.....idk















