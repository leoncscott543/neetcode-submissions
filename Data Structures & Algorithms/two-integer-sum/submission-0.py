# find 2 indices in array nums that add to "target"... cant be the same indice

# are we optimizing for space or time? 
# they MUST be ints right? should i take care of accidents?

''' ###
ok lets solve this:

Brute: 
- nested traversal
- add inner loop and outer loop 
- if nums[i] == nums[j] and i!=j return True
- else return False (out of the scope of the loop)
- time is On^2, space = On

Slightly Better:
- Two Pointers
- Create copy of array and sort in ascending order
- initialize two pointers, one at beginning (i), one at ending (j) of array
- iterate through array with two pointerse
        - check if sum of the two #s is equal to the target
- if sum is equal to target, return indices of two nums
- if sum is less than or equal to target, move the left pointer i to the right
- if sum is greater than target, move the right pointer j to the left, decrease the sum
- garenteed to be exactly one solution so we will never return empty array
- time Ologn, space On

Btr:
- store in hash/dict
- as we store:
- if dict contains a value such that nums[i] + value = target, return True
- else return false (out of scope of the loop)
- time = O(n) space = O(n)

Pay attention to what is being asked:
     you need to return the indicies, not true or false!
lets implement this 

### '''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []