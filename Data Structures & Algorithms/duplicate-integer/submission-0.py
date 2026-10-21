# find duplicate values in nums[], return true if you find a pair
# brute, traverse list with nested loop
# return true if outer nums[i] = inner nums[c]
# time = exp, space = O[1]

# better solution, store in binary tree
# return true if we have a collision of same int
# store in a dict/hash
# return true if we have a collision

# we can do binary sort too, which will be 0[1] space, but Ologn time
# space is cheaper than time. If we are optimizing for space then this is best solution
# or we can do hash and simply delete array as we traverse

# time = O[n] worse case
# space = [O[n] worse case
# this is is my best solution 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        # if we exit loop that means there's nothing found 
        return False

            