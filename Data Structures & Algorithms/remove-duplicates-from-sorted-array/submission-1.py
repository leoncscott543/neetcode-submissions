'''
traverse the nums list in order
if curr value == prev value, pop current element from array

Implementation:
- while loop
- traverse from 0 to length of nums
- if curr == prev, pop curr
- increment incremental by 1
- out of scope of loo
    - return k (size of nums)

time = On, space O(1)
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):

            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i = i + 1

        k = len(nums)
        return k