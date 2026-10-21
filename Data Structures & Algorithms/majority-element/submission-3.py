"""
given nums of size n, return majority element in array
assume there exist a majority element

Only logical non insane way of solving this i can think of: 
- Hash the entire array...
- increase key according to instances of value
- return max key's value

Time = 0(n)
Space = O(n)

implementation:
- create empty dict
- traverse nums and hash each element
- if current dict contains the curr trav element, increment key
- else just store like normal?
- return the largest key's value

******** 
slight correction:
key = element
value = occurance

collections.Counter class is super useful
function: counter(list/arr) stores array as dict of all elements in array as KEYS and occurances of each element as COUNTER

new implementation: 
- use counter to make a new dict using nums of elements as keys and instances of  each element as values
- return count[maxkey's element]
- time On, space On

can we solve this in 0(1) space complexity? 

im confused, are there only 2 different ints in the nums array?

Input: nums = [5,5,1,1,1,5,5]


""" 
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        keepCount = Counter(nums)
        return max(keepCount, key = keepCount.get)