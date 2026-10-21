# return true if s and t are anagram strings
# sort both strings, if they equal return true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False