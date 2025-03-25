class Solution:
    def romanToInt(self, s: str) -> int:
        roman_integer = [
                            ("I", 1), 
                            ("V", 5), 
                            ("X", 10), 
                            ("L", 50), 
                            ("C", 100), 
                            ("D", 500), 
                            ("M", 1000)
                        ]
        
        roman_integer_dict = dict(roman_integer)
        total = 0
        prev = 0

        for i in range(1, len(s)):
            if roman_integer_dict[s[prev]] < roman_integer_dict[s[i]]:
                total -= roman_integer_dict[s[prev]]
            else:
                total += roman_integer_dict[s[prev]]
            prev = i

        total += roman_integer_dict[s[prev]]

        return total
    
s = "MCMXCIV"
print(Solution().romanToInt(s))