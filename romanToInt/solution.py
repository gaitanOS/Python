class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        intValue = 0
        for i, rn in enumerate(s):
            if i + 1 < len(s) and romanNumerals[s[i]] < romanNumerals[s[i + 1]]:
                intValue -= romanNumerals[rn]            
            else:
                intValue += romanNumerals[rn]
                
        return intValue