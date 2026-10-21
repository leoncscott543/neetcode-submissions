# given array of strings, return longest common prefix
# strs length greater than or equal to 1 and less than equal to 200 
# string within the array  is greater than equal to 0 and less than equal to 200
# string within array made up of all lowercases and is non empy

'''
brute:
- longest common cannot be any bigger than smallest string
- every string in array must be a part of longest possible string
- sort list
- nested loop to check each string character by character against the next ones in the array
- starting with full string, then decrementing the amount of characters
- if one doesnt equal then break and decrement
- keep doing this until we get all True's with each check
- time is exp, space is linear

return the remaining string

Faster: 
- maybe store all possible prefixes of the size of smallest prefix in a hash dict
- keep track of instances of each prefix 
- if we get an instance count equal to the the amount of strings in the subarray, then we've found our prefix
- if we don't ever get one, we return "" 
- Time Complexity = 0(nlogn) (sorting list), m being the size of the strings which cant be larger than 200.... 0(n*m) space

* actually we dont need to sort, we can just find the min(length) string in the strs array (way too overthought)
Implemntation
- create a dictionary
- extract min string from strs
- loop through the strs
- loop through the lengths of the string within strs
- store every prefix from index 0 to the length of the min string into hash map
- idk how to deal with occurannces using a key or something within the hashmap
- whenever that value's key reaches length of the strs (which is a checker before each hash store) return that value in store
- else (outside scope of the loop) return "" 

Better idea: 
- we only need to compare the same index across the each string
- if the first index 0 isnt universal, automatically return ""
- lets loop up to the size of the min string 0 -> min string len
- we check each character in each string to determine if there's a match
- whenever we hit a mismatch, we return the string of 0->index right before mismatch
- time complexity: O(m) where m is the size of the min string, 0(1) space

Implementation:
- find min and store min string <
- loop through strs from 0 to min string length <
- if strs[i][0] != minstring[c] return ""
- if strs[i][c] != minstring[c] return minstring in the range of 0 to c

Ok better implementation: 
- keep the min code, thats useful
- traverse the 

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        for i, strings in enumerate(strs):
            for c in range(len(smallest)):
                if strs[i][0] != smallest[0]:
                    return ""
                if strs[i][c] != smallest[c]:
                    smallest = smallest[:c]
                    break
        return smallest