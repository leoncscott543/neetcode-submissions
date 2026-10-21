'''
- given an array of strings: group all anagrams into sublists
- medium problem
- sublist can be of any size

constraints:
- 1 <= strs length <=1000
- 0 <= substring <= 100
- substring is all lowercase

Brute: 
- sort each substring
- nested traversal to find matching new substrings
- store each match in a new array
- match the list back together into a new list

Better: 
- sort each substring
- store both string and the instance each appears in hashmap into hashmap
- time complex.... Ologn time (sorting) O(n) space

- implementation: 
- instantiate a dict
- instantiate an outerlist
- traverse list and sort and store in hash table <
- create a new list with the lists of each anagram


'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for string in strs:
            # sorted string acts as the key for anagrams
            sorted_str = "".join(sorted(string))
            if sorted_str not in store:
                store[sorted_str] = []
            store[sorted_str].append(string)

        return list(store.values())