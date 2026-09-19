class Solution:
    def isPalindrome(self, s: str) -> bool:
        test_string=""
        for i in s:
            if i.isalnum():
                test_string=test_string+i.lower()
        print(test_string)
        return test_string==test_string[::-1]