class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize tracking variables with the first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Either add the current number to the existing subarray 
            # or start a new subarray from the current number
            current_sum = max(num, current_sum + num)
            
            # Update the global maximum sum found so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum
