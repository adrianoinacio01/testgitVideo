# Valid Anagram
# Given two strings s and t, 
# return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.
# s and t consist of lowercase English letters.

# Inputs:
# racecar and carrace -> true
# jar and jam -> false
# xx and x -> False
# bbcc and ccbc -> False

''' Solution 01, using Counter
It's very simply... Counter (s) == Counter (t)
Counter used to compare occurences into s and t
    
    Solution 02, using sorted
using solution showed in neetcode but a little different
step 1: len(s) == len (t) if and only if sorted equal
sorted order all characters
'''
# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str):
        #print(sorted(t),sorted(t))
        return len(s) == len(t) if (sorted(t) == sorted(s)) else False
        # return Counter(s) == Counter(t)
        # if set(s) == set(t):
        #     if len(s) == len(t):
        #         if set(list(filter(str.isalpha,t))) == set(list(filter(str.isalpha,s))):
        #             return True
        #         else:
        #             return False
        #     else:
        #         return False
        # else:
        #     return False
        # print(
        #     set(s) == set(t),
        #     len(s) == len(t),
        #     set(list(filter(str.isalpha,t))) == set(list(filter(str.isalpha,s))),
        # )
        # return (list(filter(str.isalpha,t))) == set(list(filter(str.isalpha,s))) if (len(s) == len(t)) or (set(s) == set(t)) else False
        # #return (set(s) == set(t)) if (len(s) == len(t)) else False
s = 'racecar'
t = 'carrace'
# s = 'jar'
# t = 'jam'
# s = 'xx'
# t = 'x'
# s = 'bbcc'
# t = 'ccbc'
# print(set(s),set(t))
# print(len(set(s)),len(set(t)))
# print((str.isalpha,t) == (str.isalpha,s))
# print(filter(str.isalpha,t),filter(str.isalpha,s))
# print(list(filter(str.isalpha,t))) , (list(filter(str.isalpha,s)))
print(Solution().isAnagram(s,t))