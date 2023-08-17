class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join([char for char in s if char.isalpha() or char.isnumeric()]).lower()
        i = 0
        length = len(filtered)
        for i in range(length):
            if filtered[i] != filtered[length - i - 1]:
                return False
        return True
