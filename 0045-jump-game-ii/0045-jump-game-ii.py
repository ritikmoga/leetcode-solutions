class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            # Current position se maximum kitna door ja sakte hain
            farthest = max(farthest, i + nums[i])

            # Current jump ki range khatam
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps