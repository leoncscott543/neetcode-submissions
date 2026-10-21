'''
- given int array nums, and target int, return indice i and j where numsi+numsj == target, and i!=j

- solution 1 is nested loop, traverse and find i,j that meets condition... expenential time complexity, 0(1) space
- solution 2 is hash nums value and index... 
- compare current value/index being hashed to current dict inventory.... 
- if there exist a value and index that meets the condition in the hash with the current value and index being hashed, return said i, j, break 
- 0(n) worse case time, 0(n) worse case space
- lets implement this

1. create emply dict
2. loop through nums and store index and val in dict
3. check for condition each traversal
    - 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # instantiate dict/hash table
        store = {}
        
        # traverse nums array by index
        for i in range(len(nums)):
            if target - nums[i] in store:
                j = store[target - nums[i]]
                return [j,i]
            else:
                store[nums[i]] = i
                print(store)
        