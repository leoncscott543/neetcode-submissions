'''
- given nums array and val int, remove all instances of val in nums, return k, new size of list
- k can also represent all non repeating elements up until repeating ones

Brute: nested comparison.... if there exist any repeating value, pop it from the original list
exp time, possibly even 0(n) space

Better solution: In place traversal
- Traverse Nums and keep track of nums[i] == nums[i-1]
    - this signals a duplicate
    - pop nums[i]
- this is 0(n) time and 0(n) space possibly because of the time it takes to shift the other elements after a pop

Better solution? Two pointers? 
- Because all that matters is that we return a k such that 0 to k represents all of the in-order unique elements in the list
- We can re-arrange the elements in this way without manipulating the structure of the array with deletion operations
- We can make a first[i] and prev prev[i-1]
    - if first == prev.... that's a duplicate

- implementation:
- create c = 1 int, only iterates when we find a duplicate followed by a non duplicate
- traverse list from i = 1 to size of nums
- if nums[i] == nums[i-1] and nums[i] != nums[i+1], 
    - nums[c] == nums[i+1]
    - increment c by 1
    - k = c
- return k

'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        i = 0
        k = 0
        
        while i < len(nums):
            if(nums[i] != val):
                nums[c] = nums[i]
                c = c + 1
                k = c
            i = i + 1
        return k