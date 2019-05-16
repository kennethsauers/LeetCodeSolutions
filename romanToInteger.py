class Solution:
    def romanToInt(self, s: str) -> int:
        lookUpDic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        numArr = []

        #these to for loops could be combined giving O(n)
        # in place of O(2n) has well as reduce space complexity

        for letter in s:
            numArr.append(lookUpDic[letter])

        sum = 0
        for i in range(len(numArr)):
            if i+1 is len(numArr):
                sum += numArr[i]
                return sum
            if numArr[i] >= numArr[i+1]:
                sum += numArr[i]
            elif numArr[i] < numArr[i+1]:
                sum -= numArr[i]


            
