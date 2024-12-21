'''
Solution alternative
using matrix sum
pairwise = vector nums transponse + vector nuns

using NumPy for
np.argwhere: select indices with criteria boolean
[:, np.newaxis]: tranponse matrix
sorted + tuple: modify de matrix indices (for sorted command)

'''
import numpy as np
class Solution:
    def twoSum(self, nums, target):
        pairwise_sums = nums[:, np.newaxis] + nums
        indices = np.argwhere(pairwise_sums == target)
        indices = sorted([tuple(row) for row in indices])
        for i,j in indices:
            if i != j:
                return [i,j]
nums = np.array([3,4,5,6])
target = 7
result = Solution().twoSum(nums, target)