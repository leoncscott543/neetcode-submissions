# take an array nums and concatenate nums onto itself
# example is [3,2,3] -> [3,2,3,3,2,3]

# quickest solution is to add the 2 arrays together: 
# time complexity is 0(n), space complexity is 0(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums