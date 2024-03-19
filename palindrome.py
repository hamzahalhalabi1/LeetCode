class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        y = "".join(reversed(x))
        return y == x

        # original_x = x
        # reversed_x = 0
        #
        # while x > 0:
        #     digit = x % 10
        #     reversed_x = reversed_x * 10 + digit
        #     x //= 10
        #
        # return original_x == reversed_x


palindrome = Solution()
result = palindrome.isPalindrome(545)
print(result)
