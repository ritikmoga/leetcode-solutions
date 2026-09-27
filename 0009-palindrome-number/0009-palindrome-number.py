class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
            
        s = str(x)
        opposite = s[::-1]
        rev = int(opposite)
        
        if rev == x:
            return True
        else:
            return False
