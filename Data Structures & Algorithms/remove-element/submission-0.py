'''
Problem: 
- Remove all instances of val:int from nums:list in place
- Return k-number of remaining elements in nums, first k elements of nums do not contain val
- order of elements not equal to val dont matter
- not neccessary to consider elements beyond the first k positions in array
constraints: small 0 -> 50/100 int contraints

Seems straight forward enough:

Brute: 
We can traverse list and build a new list only with values != val
Return length of new list
Time = On (worse case if there is no val instance in nums), space On, for new list if every element=val in nums

faster? 
well better is the question, we need to remove inplace. not create new list
just .remove() each instance of val, 0(n) time complexity unless end of the list which is 0(1)
Space complexity is 0(1), so this is a better overall solution

Impement: 
traverse nums from 0 to length of list <
if nums[i] = val, nums.remove(nums.i) <
i think nums size will be updated as this goes on in loop <
return k out of scope of the loop <

test: 
Input: nums = [0,1,2,2,3,0,4,2], val = 2
l1 - != val
l2 - != val
l3 - == val remove 
l4 - == val remove 
l5 - != val
l6 - != val
l7 - != val
l8 - == val remove 

set k = new length of nums
return k


*****************************
classic issue where you are removing an element and iterating over it, skipping next element after one is removed because iteration limit count also changes

the solution is to make a clever while loop (while val is in list, remove val.... this ensures that the loop continues until all first occurances of val are gone)
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        k = len(nums)
        return k