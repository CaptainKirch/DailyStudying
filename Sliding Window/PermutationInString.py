# Problem Statement:
# Given two strings s1 and s2, return True if s2 contains a permutation of s1, or False otherwise.

# In other words, check if any substring of s2 is an anagram of s1.

# from collections import Counter # This is adding the Counter method into the function, which creates counts in dicts.

# def checkInclusion(s1, s2):
#     if len(s1) > len(s2): #Handling edge case of if the leng of the first array is longer than the second it can't be a permutation so we return False.
#         return False
    
#     s1_count = Counter(s1) # We assign a variable of s1_count to Counter to count the entire array of s1.
#     window_count = Counter(s2[:len(s1)]) #We assign window_count to Counter of just the beginning of string of s2 to s1 length, which allows us to check if the substring of s1 is the same as a substring of s2.

#     if window_count == s1_count: #This is checking if the window_count is identical immediately in the substring, in the beginnnig to return True instead of needing to waste time going through the entire string.
#         return True

#     for i in range(len(s1), len(s2)): #A for loop over the length of s1 to s2 length.
#         start_char = s2[i - len(s1)] #We then are setting the sliding window with start_char as the beginnig of the window. And new_char as another side of the window.
#         new_char = s2[i]

#         window_count[new_char] += 1 # Increasing the window and decreasing the window for each string.
#         window_count[start_char] -= 1

#         if window_count[start_char] == 0: # if statement asking if any char's in the counter dict is equal to zero we delete it out of the coutner.
#             del window_count[start_char]

#         if window_count == s1_count: # If the window_count which is s2 and included items inside the counter dict for frequency are identical to s1_count, we return True
#             return True
        
#     return False # And if all else is false we return False.


# print(checkInclusion("ab", "eidbaooo"))   # True → "ba" is a permutation
# print(checkInclusion("ab", "eidboaoo"))   # False → no permutation
# print(checkInclusion("adc", "dcda"))      # True → "dca" is a permutation
# print(checkInclusion("a", "a"))           # True
# print(checkInclusion("ab", "a"))          # False

# from collections import Counter

# def checkInclusion(s1, s2):
#     if len(s1) > len(s2):
#         return True
    
#     s1_count = Counter(s1)
#     window_count = Counter(s2[:len(s1)])


#     if s1_count == window_count:
#         return True
    
#     for i in range(len(s1), len(s2)):
#         start_char = s2[i - len(s1)]
#         new_char = s2[i]


#         window_count[new_char] += 1
#         window_count[start_char] -= 1


#         if window_count[start_char] == 0:
#             del window_count[start_char]

        
#         if window_count == s1_count:
#             return True
        
#     return False


# print(checkInclusion("ab", "eidbaooo"))
# # True

