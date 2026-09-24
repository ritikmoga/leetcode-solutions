class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()

        expected = 1

        for num in nums:
            if num == expected:
                expected += 1
            elif num > expected:
                return expected

        return expected