class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
    
        }
        s = s.replace('IV', 'IIII')
        s = s.replace('IX', 'VIIII')
        s = s.replace('XC', 'LXXXX')
        s = s.replace('CM', 'DCCCC')
        s = s.replace('CD', 'CCCC')
        s = s.replace('XL', 'XXXX')
        k = 0
        for i in s:
            k+= dic[i]
        return k

sol = Solution()
print(sol.romanToInt('MMMXLV'))
