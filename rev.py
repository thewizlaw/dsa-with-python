class Solution:
    def reverse(self, x: int) -> int:
        new = abs(x)
        new = str(new)
        new = new[::-1]
        new = int(new)
        
        if x < 0:
            new = -new
        
        if new < -2**31 or new > 2**31 - 1:
            return 0
        else:
            return new
        