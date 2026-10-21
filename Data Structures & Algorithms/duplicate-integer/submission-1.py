# return true if nums[] contains duplicte val, else return false
# all ints
# no special chars
# inf  possibiliites
# return on first find
# optimize time complex

# brute force, nested loop, traverse inner and outer nums[] until we find a match
# too slow, exp time 

# more optimized for space, slightly faster time:
# sort in place, stop when we find a match
# binary sort, quicksort
# Olog(n) time, 0(1) space

# time optimized
# store in new hashmap
# stop when we have collision
# this 0(n) time and space complex, linear

# test: 1,4,5,4

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        find = {} 

        for data in nums:
            if data in find: # key check
                return True
            else:
                find[data] = True # if not, add data to dict
        return False # return true with no match 

        