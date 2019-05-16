class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numArr = (self.intToString(x))
        halfLen = int(len(numArr) / 2)
        for i in range(halfLen):
            if numArr[i] is not numArr[len(numArr) - 1 - i]:
                return False
        return True

    def intToString(self, x: int) -> list:
        numArr = []
        while x is not 0:
            numArr.append(x%10)
            x = int(x / 10)
        return numArr
