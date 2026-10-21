'''
- given an array of strs strs
- return longest common prefix
- return "" empty string if there is no longest common pre

- brute
- nested comparison against of each index in each string in order....
- horrible time complexity, exp time, constant space

2. better
- horizontal index checker
- traverse each string in strs by common index
- as soon as we find uncommon character at common index, return remainder of string up until then
- that will be longest common prefix
- only need to traverse the length of shortest string (longest potential prefix)
- if we never find an uncommon character while traversing common indexes, return shortest string
- time = 0(N*L) L being shortest string, space = 0(1)

Implementation: 
1. initialize min string in array
2. traverse array from 0 to length of array
3. within this traverse strings from 0 to length of shortest string
4. if min string [c] != curr[c], return minstring[:-1] ()
5. outside of scope of both loops, return ""

Test: 
input: ["bat","bag","bank","band"]
minstring  = "bat"
- traverse:
    - no thats not index
    - 
- array length >= 1 and less equal to 200
- made up of all lower cases
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstring = min(strs)

        for i in range(len(strs)):
            for c in range(len(minstring)):
                if strs[i][c] != minstring[c]:
                    return minstring[:c]

        return minstring
        