class Solution(object):
    roman = {
        "I" :1,
        "V": 5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
    def romanToInt(self, s):
        total = 0
        for x in range(0,len(s)):
            if x == len(s)-1:
                total += Solution.roman[s[x]]
            elif Solution.roman[s[x]] < Solution.roman[s[x+1]]:
                total-=Solution.roman[s[x]]
            else:
                total+=Solution.roman[s[x]]
        return(total)
x = Solution()
s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"
x.romanToInt(s2)
x.romanToInt(s3)


