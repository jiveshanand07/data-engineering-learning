'''
Docstring for problems.week.week-01.day-1-two-sum
'''

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        print(f"Outer loop: i = {i}") 
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i,j]



'''
TO mak ethis better we need to think in apattern that which number is the one that I need. i.e. complemnent..
but in dictionary we will store the scanned numbers nbbut compare it with complemerent
'''

nums = [2, 7, 11, 15]
target = 9
print("Final Result", twoSum(nums, target))


def two_sum_optimized(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen.get(complement), i]
        else:
            seen[num] = i
    
    return []
