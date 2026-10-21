# determine if str s and t are anagrams, same characters different order
# s and t dont necessarily have to be the same length

# 1. if s and t are different lengths, return false
# 2. sort s and t, and compare them
# 3. if we sort them and s != t, return false
# 4. else return true

# if we sort in place this is Ologn time, 0(1) space

# Test 1: s = ijfew, t  = we, length of s != length of t, returns false
# Test 2: s = wj, t = wf, sorted s = jw, sorted t = fw, dont equal, return false
# Test 3: s = dfs, t = sfd, sorted s = dfs, sorted t = dsf, they equal, return True 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if sorted(s) != sorted(t):
            return False
        else:
            return True
        