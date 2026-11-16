class Solution:
    def findMissingElements(self, nums):
        present = set(nums)
        return [num for num in range(min(nums), max(nums) + 1) if num not in present]