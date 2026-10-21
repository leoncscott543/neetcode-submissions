# given array nums... length n
# make ans[] of length 2n where ans[i] == nums[i] and ans[i+1]==nums[i]
# for 0<= i < n

# summary,so basically concatenation of 2 nums arrays
# return ans

# example [1,4,1,2]
# return [1,4,1,2,1,4,1,2,1]

# you can just traverse the list twice wiith 2 loops in series
# time complexity, O(N)
# space complexity, O(2) - we have to allocate a new array of twice the size of nums

# second idea, set ans equal to 2 nums[]

# Good job leon! got it right first attempt, might be optimal solution! 

# how could we make this faster?
# Im not sure  there is a way, lets check 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
        
