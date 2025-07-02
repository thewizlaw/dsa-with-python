class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for char in s:
            if char.isalnum():
                result+=char
        result = result.lower()

        if result == result[::-1]:
            return True
        else:
            return False