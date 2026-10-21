'''
given nums array and int k, return k-most frequent elements in array

so if k = 3, we are looking for the 3 most frequent elements
and if k = 1, we are looking for THE most frequenet element

so you're returning a list of ints of the most freq elements according to the k-value

The only thing that comes to my mind is a dictionary/hash:
- Using the collections lib, Counter method
- stores key as elements, value as instances of each element.... into the dict
- then retrieve the value of the k top instances into a append them to a new list

Time O(n), Space O(n)

Implementation:
- create empty dict
- traverse nums
- set each element equal to Counter(nums[i])
- Make a new loop from size of nums to 0 
- if dict_value != NULL, append to newlist
- decrement c

Can we improve space complexity? 
- possibly with two pointers, but i dont have the mental capacity to figure that out right now... 

'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        duplicates = {}
        i = 0
        c = 0

        duplicates = Counter(nums) # hashes nums into duplicates as keys(element), and value(occurances), in order from most frequent to least

        sorted_duplicates = dict(sorted(duplicates.items(), key=lambda item: item[1], reverse=True))

        # get a list of only the keys in order from most frequent to least 
        keylist = list(sorted_duplicates.keys())
        top_duplicates = keylist[:k]

        return top_duplicates