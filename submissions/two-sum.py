// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = [];
        for i in range(len(nums)):
           for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                       temp += [i]
                       temp += [j]
        return temp
                       