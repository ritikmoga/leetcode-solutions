class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # Binary search pointers for the smaller array
        l, r = 0, len(A) - 1
        
        while True:
            # Partition index for A
            i = (l + r) // 2  
            # Partition index for B
            j = half - i - 2  
            
            # Boundary values around the partitions
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements
                if total % 2:
                    return min(Aright, Bright)
                # Even total elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright:
                r = i - 1  # Move left in A
            else:
                l = i + 1  # Move right in A
