'''
Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Input: strs = ["x"]
Output: [["x"]]

Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''
# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str):
#         return Counter(s) == Counter(t)
# s = 'xx'
# t = 'x'
# print(Solution().isAnagram(s,t))  

# test 1: understand Counter from collections
# from collections import Counter
# nums = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3]
# count = Counter(nums)
# print(count[6])
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length_dict = defaultdict(list)
        for word in strs:
            word_length = len(word)
            length_dict[word_length].append(word)
            # print(length_dict)
            # print(word,len(word))
        return list(length_dict.values())

strs = ["act","pots","tops","cat","stop","hat"]
solution = Solution()
result = solution.groupAnagrams(strs)
print(len(result))
# print(Solution().groupAnagrams(strs))