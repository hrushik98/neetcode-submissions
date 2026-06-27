class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100,
            "D": 500, "M": 1000
        }
        
        ans = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s):
                if (s[i] == "I" and s[i+1] in ["V", "X"]):
                    ans += hmap[s[i+1]] - 1
                    i += 2
                    continue
                elif (s[i] == "X" and s[i+1] in ["L", "C"]):
                    ans += hmap[s[i+1]] - 10
                    i += 2
                    continue
                elif (s[i] == "C" and s[i+1] in ["D", "M"]):
                    ans += hmap[s[i+1]] - 100
                    i += 2
                    continue

            ans += hmap[s[i]]
            i += 1

        return ans